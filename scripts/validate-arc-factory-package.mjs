#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';

const arcDir = path.resolve(process.argv[2] || 'arc');
const errors = [];
const warnings = [];

const requiredPaths = [
  'FACTORY-BIRTH-MANIFEST.json',
  'README.md',
  'REPOSITORY-SOURCE-BOUNDARY.md',
  'access-policy.json',
  'BRAINS/README.md',
  'governance/COMMERCIAL-ENTITLEMENT.md',
  'visual/ARC-VISUAL-IDENTITY.md',
  'visual/visual-identity.json',
  'onboarding/FIRST-CONTACT.md',
  'runtime/README.md',
  'bridge/STATE.json',
  'evidence/README.md'
];

function fail(message) { errors.push(message); }
function warn(message) { warnings.push(message); }
function exists(rel) { return fs.existsSync(path.join(arcDir, rel)); }
function read(rel) { return fs.readFileSync(path.join(arcDir, rel), 'utf8'); }
function parseJson(rel) {
  try { return JSON.parse(read(rel)); }
  catch (err) { fail(`${rel}: invalid JSON (${err.message})`); return null; }
}

if (!fs.existsSync(arcDir) || !fs.statSync(arcDir).isDirectory()) {
  console.error(`ARC Factory validation FAILED: not a directory: ${arcDir}`);
  process.exit(2);
}

for (const rel of requiredPaths) {
  if (!exists(rel)) fail(`missing required path: ${rel}`);
}

const instanceCandidates = fs.readdirSync(arcDir)
  .filter((name) => name.endsWith('_INSTANCE.json'));
if (instanceCandidates.length !== 1) {
  fail(`expected exactly one *_INSTANCE.json, found ${instanceCandidates.length}`);
}

const manifest = exists('FACTORY-BIRTH-MANIFEST.json')
  ? parseJson('FACTORY-BIRTH-MANIFEST.json') : null;
const instance = instanceCandidates.length === 1
  ? parseJson(instanceCandidates[0]) : null;
const access = exists('access-policy.json') ? parseJson('access-policy.json') : null;
const visual = exists('visual/visual-identity.json') ? parseJson('visual/visual-identity.json') : null;
const bridge = exists('bridge/STATE.json') ? parseJson('bridge/STATE.json') : null;

const safeControlKeys = new Set([
  'secrets_outside_git',
  'secrets_in_git_allowed',
  'credentials_in_repository_allowed',
  'credentials_in_git_allowed',
  'personal_numeric_identifiers_in_repository_allowed'
]);

function walk(value, keyPath = '$') {
  if (typeof value === 'string') {
    if (/\{\{[^}]+\}\}/.test(value)) fail(`${keyPath}: unresolved template placeholder`);
    return;
  }
  if (Array.isArray(value)) {
    value.forEach((v, i) => walk(v, `${keyPath}[${i}]`));
    return;
  }
  if (!value || typeof value !== 'object') return;

  const forbiddenKey = /(token|secret|password|api[_-]?key|private[_-]?key|credential)/i;
  for (const [key, val] of Object.entries(value)) {
    if (forbiddenKey.test(key) && !safeControlKeys.has(key) && val !== null && val !== false) {
      fail(`${keyPath}.${key}: secret/credential-like field must not contain repository payload`);
    }
    walk(val, `${keyPath}.${key}`);
  }
}

for (const [name, doc] of Object.entries({ manifest, instance, access, visual, bridge })) {
  if (doc) walk(doc, name);
}

if (manifest) {
  const requiredManifestKeys = [
    'factory_contract_version',
    'factory_template_version',
    'arc_id',
    'display_name',
    'production_state',
    'source_boundary',
    'owner',
    'language',
    'commercial',
    'runtime',
    'hermetic_seal',
    'operator_access',
    'intelligence_policy',
    'visual',
    'registries',
    'maturity',
    'provenance',
    'stages'
  ];
  for (const key of requiredManifestKeys) {
    if (!(key in manifest)) fail(`manifest: missing required field ${key}`);
  }

  if (!/^[a-z0-9][a-z0-9-]*$/.test(manifest.arc_id || '')) {
    fail('manifest.arc_id: invalid stable ARC ID');
  }

  const sb = manifest.source_boundary || {};
  if (!['ryz3n_owned_product_domain', 'customer_standalone_domain'].includes(sb.class)) {
    fail('manifest.source_boundary.class: invalid repository class');
  }
  if (!sb.authoritative_repository || !sb.arc_root) {
    fail('manifest.source_boundary: authoritative_repository and arc_root required');
  }
  if (sb.arc_root !== 'arc/') warn(`manifest.source_boundary.arc_root is ${sb.arc_root}, expected canonical arc/ unless explicitly justified`);

  const hermetic = manifest.hermetic_seal || {};
  if (!['inherited_pre_runtime', 'hardening_in_progress', 'GREEN', 'DRIFT', 'RED'].includes(hermetic.status)) {
    fail('manifest.hermetic_seal.status: invalid status');
  }
  if (hermetic.maturity_promotion_implied !== false) {
    fail('manifest.hermetic_seal: maturity_promotion_implied must be false');
  }
  if (hermetic.safe_shared_writer_required_if_autonomy_granted !== true) {
    fail('manifest.hermetic_seal: safe shared writer must be required if autonomy is granted');
  }

  const operator = manifest.operator_access || {};
  if (operator.founder_operator_role_separate_from_owner !== true) {
    fail('manifest.operator_access: Founder operator must remain a role separate from Owner');
  }
  if (operator.founder_operator_owner_private_memory_access_allowed !== false) {
    fail('manifest.operator_access: Founder operator must not inherit Owner-private memory access');
  }
  if (operator.founder_operator_cross_arc_private_state_access_allowed !== false) {
    fail('manifest.operator_access: Founder operator must not gain cross-ARC private-state access');
  }
  if (operator.own_repo_write_requires_bounded_safe_writer !== true) {
    fail('manifest.operator_access: autonomous own-repo writes require bounded safe-writer plumbing');
  }

  const intel = manifest.intelligence_policy || {};
  const freeOnlyChecks = [
    ['free_endpoint_required', true],
    ['paid_model_fallback_allowed', false],
    ['autonomous_billing_changes_allowed', false],
    ['autonomous_credit_purchase_allowed', false],
    ['deterministic_eol_failover_without_retry_storm', true]
  ];
  for (const [key, expected] of freeOnlyChecks) {
    if (intel[key] !== expected) fail(`manifest.intelligence_policy.${key}: expected ${expected}`);
  }
  if (intel.paid_override_authority !== 'founder_explicit_only') {
    fail('manifest.intelligence_policy.paid_override_authority must be founder_explicit_only');
  }

  if (manifest.maturity?.verified === false && manifest.maturity?.earned_aura) {
    fail('manifest.maturity: cannot have earned aura while maturity is unverified');
  }

  const s = manifest.stages || {};
  const order = [
    'F0_authorization',
    'F1_source_boundary',
    'F2_instance_package',
    'F3_stewardship_registration',
    'F4_runtime_provisioning',
    'F5_owner_binding_first_run',
    'F6_evidence_closeout'
  ];
  let seenPending = false;
  for (const stage of order) {
    const value = String(s[stage] ?? 'missing');
    const complete = value.startsWith('complete');
    if (seenPending && complete) fail(`manifest.stages: ${stage} complete after an earlier pending stage`);
    if (!complete) seenPending = true;
  }

  if (String(s.F4_runtime_provisioning).startsWith('complete') && manifest.runtime?.status === 'not_provisioned') {
    fail('manifest: F4 complete but runtime.status is not_provisioned');
  }
  if (String(s.F5_owner_binding_first_run).startsWith('complete') && String(manifest.owner?.binding_status).includes('pending')) {
    fail('manifest: F5 complete but owner binding remains pending');
  }
}

if (manifest && instance) {
  if (manifest.arc_id !== instance.arc_id) fail('cross-check: manifest.arc_id != instance.arc_id');
  if (manifest.display_name !== instance.display_name) fail('cross-check: manifest.display_name != instance.display_name');
  if (manifest.source_boundary?.authoritative_repository !== instance.repository_boundary?.authoritative_repository) {
    fail('cross-check: authoritative repository differs between manifest and instance');
  }
}

if (manifest && bridge) {
  if (manifest.arc_id !== bridge.arc_id) fail('cross-check: manifest.arc_id != bridge.arc_id');
  if (bridge.authoritative_repository && bridge.authoritative_repository !== manifest.source_boundary?.authoritative_repository) {
    fail('cross-check: bridge authoritative repository differs from manifest');
  }
}

if (access) {
  if (access.secrets_in_git_allowed === true) fail('access-policy: secrets_in_git_allowed must not be true');
  if (access.credentials_in_repository_allowed === true) fail('access-policy: credentials_in_repository_allowed must not be true');
  if (access.cross_arc_private_state_access === true) fail('access-policy: cross_arc_private_state_access must not be true');
  if (access.default_policy && !String(access.default_policy).includes('deny')) {
    warn('access-policy: default policy is not explicitly deny/fail-closed');
  }
}

if (visual) {
  if (visual.maturity_aura?.earned === true && !visual.maturity_aura?.verified_maturity) {
    fail('visual identity: earned aura without verified maturity');
  }
  if (visual.founder_owner_approved === false && visual.current_asset_status === 'canonical') {
    fail('visual identity: unapproved asset cannot be canonical');
  }
}

if (manifest?.source_boundary?.domain_verification && /unverified/i.test(manifest.source_boundary.domain_verification)) {
  warnings.push('candidate hostname/domain remains unverified; production DNS/deploy must stay blocked');
}

if (warnings.length) {
  console.log('ARC Factory validation warnings:');
  warnings.forEach((w) => console.log(`  - ${w}`));
}

if (errors.length) {
  console.error('ARC Factory validation FAILED:');
  errors.forEach((e) => console.error(`  - ${e}`));
  process.exit(1);
}

console.log(`ARC Factory validation PASS: ${arcDir}`);
process.exit(0);
