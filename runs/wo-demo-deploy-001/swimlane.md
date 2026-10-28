# Swimlane

Cost is reported as null here. Model runtimes report cost when they run a station; ANVIL never invents a number.

| Station | Status | Duration ms | Artifacts | Cost |
|---|---|---|---|---|
| intake | completed | 0.021 | runs/wo-demo-deploy-001/report.json | null |
| spec-writer | executed | 48.017 | runs/wo-demo-deploy-001/spec-writer.output.md | null |
| test-writer | executed | 45.558 | runs/wo-demo-deploy-001/test-writer.output.md | null |
| builder | executed | 44.374 | runs/wo-demo-deploy-001/builder.output.md | null |
| reviewer-spec | executed | 44.632 | runs/wo-demo-deploy-001/reviewer-spec.output.md | null |
| reviewer-security | executed | 46.834 | runs/wo-demo-deploy-001/reviewer-security.output.md | null |
| reviewer-tests | executed | 77.666 | runs/wo-demo-deploy-001/reviewer-tests.output.md | null |
| reviewer-architecture | executed | 82.752 | runs/wo-demo-deploy-001/reviewer-architecture.output.md | null |
| approver | completed | 0.044 | runs/wo-demo-deploy-001/report.json | null |
| triage-human | completed | 0.014 | - | null |
| deployer | executed | 165.27 | runs/wo-demo-deploy-001/deployer.output.md | null |
| verifier | executed | 90.331 | - | null |
| observer | executed | 44.99 | runs/wo-demo-deploy-001/observer.output.md | null |

Deployment: deployed_verified

Verification:
- pass: sh -c 'cd deploy/$ANVIL_WORK_ORDER_ID && python3 -m unittest discover -s tests'
