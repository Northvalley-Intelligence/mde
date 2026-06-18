# Regenerate Website Assessment

## Inputs

- `demand-data-generation` outputs
- Website target or client data
- Assessment configuration

## Steps

1. Check latest `demand-data-generation` event.
2. Verify data schema version.
3. Run `local-website-growth-assessment`.
4. Validate report output.
5. Record `artifact_generated` event.
6. Check whether `proposals` must be regenerated.

