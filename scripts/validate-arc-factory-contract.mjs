#!/usr/bin/env node

import fs from 'node:fs';

const schemaPath = '12-arc-productization/ARC-FACTORY-BIRTH-MANIFEST-SCHEMA.json';
const templatePath = '12-arc-productization/factory-template/FACTORY-BIRTH-MANIFEST.template.json';

const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
const template = JSON.parse(fs.readFileSync(templatePath, 'utf8'));
const errors = [];

for (const key of schema.required || []) {
  if (!(key in template)) errors.push(`template missing schema-required key: ${key}`);
}

if (schema.$id !== 'ryz3n://arc-factory-birth-manifest/v1.3') {
  errors.push(`unexpected schema id: ${schema.$id}`);
}
if (template.factory_contract_version !== '1.3') {
  errors.push(`template factory_contract_version must be 1.3, got ${template.factory_contract_version}`);
}
if (template.factory_template_version !== 'factory-template-v1.3') {
  errors.push(`template factory_template_version must be factory-template-v1.3, got ${template.factory_template_version}`);
}

const hermetic = template.hermetic_seal || {};
if (hermetic.safe_shared_writer_required_if_autonomy_granted !== true) {
  errors.push('template must require bounded safe writer when autonomy is granted');
}
if (hermetic.maturity_promotion_implied !== false) {
  errors.push('hermetic seal must never imply maturity promotion');
}

const op = template.operator_access || {};
if (op.founder_operator_role_separate_from_owner !== true) {
  errors.push('Founder operator must remain separate from Owner');
}
if (op.founder_operator_owner_private_memory_access_allowed !== false) {
  errors.push('Founder operator must not inherit Owner-private memory');
}
if (op.founder_operator_cross_arc_private_state_access_allowed !== false) {
  errors.push('Founder operator must not gain cross-ARC private-state access');
}
if (op.own_repo_write_requires_bounded_safe_writer !== true) {
  errors.push('own-repo writes must require bounded safe-writer plumbing');
}

const intel = template.intelligence_policy || {};
const expected = {
  free_endpoint_required: true,
  paid_model_fallback_allowed: false,
  autonomous_billing_changes_allowed: false,
  autonomous_credit_purchase_allowed: false,
  paid_override_authority: 'founder_explicit_only',
  deterministic_eol_failover_without_retry_storm: true
};
for (const [key, value] of Object.entries(expected)) {
  if (intel[key] !== value) errors.push(`intelligence_policy.${key} must equal ${JSON.stringify(value)}`);
}

const serialized = JSON.stringify(template);
for (const forbidden of ['minimax-m3', 'paid_model_fallback_allowed":true', 'cross_arc_private_state_access_allowed":true']) {
  if (serialized.includes(forbidden)) errors.push(`template contains forbidden/stale marker: ${forbidden}`);
}

if (errors.length) {
  console.error('ARC Factory contract validation FAILED');
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log('ARC Factory contract validation PASS: schema v1.3 and template v1.3 are aligned');
