# Swimlane

Cost is reported as null here. Model runtimes report cost when they run a station; ANVIL never invents a number.

| Station | Status | Duration ms | Artifacts | Cost |
|---|---|---|---|---|
| intake | completed | 0.017 | runs/wo-gh-3/report.json | null |
| builder | executed | 40761.09 | runs/wo-gh-3/builder.output.md | null |
| reviewer-spec | executed | 35511.95 | runs/wo-gh-3/reviewer-spec.output.md | null |
| reviewer-security | executed | 45903.492 | runs/wo-gh-3/reviewer-security.output.md | null |
| approver | completed | 0.037 | runs/wo-gh-3/report.json | null |
| triage-human | completed | 0.011 | - | null |
| deployer | executed | 93.196 | runs/wo-gh-3/deployer.output.md | null |
| verifier | executed | 62.769 | - | null |

## Decision

- Approver: All counted reviews passed.
- Human gate: Verdict approved and no risk hints matched (scanned: auth, payments, data-deletion, production-deploy, secrets, publishing), so no human is required.

Deployment: deployed_verified

Verification:
- pass: sh -c 'cd deploy/$ANVIL_WORK_ORDER_ID && python3 -m unittest discover -s tests'
