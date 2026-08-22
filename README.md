# F88 | Agentic Energy Systems | L3 Gold Standard | v1.0

A governed multi-agent reference system for grid planning, generation mix, storage analysis, reliability, evidence review, uncertainty handling, and qualified human approval.

## Gold-standard governance

F88 is fail closed. Analysis release requires review of grid constraints, generation assumptions, storage assumptions, reliability, resource adequacy, stability, evidence provenance, uncertainty, and explicit qualified human approval.

Release is blocked for reliability violations, unresolved resource-adequacy gaps, exceeded stability limits, unresolved transmission constraints, invalid storage assumptions, missing evidence provenance, uncharacterized uncertainty, or unsupported operational claims.

The reference system cannot issue grid-control or dispatch commands, operate breakers, override protection, autonomously bid into markets, or autonomously shed load.

## Verification gates

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out energy-systems suite. The governed smoke path invokes the real orchestration pipeline rather than a placeholder response.
