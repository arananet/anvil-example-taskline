# Taskline

![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue) ![License Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green) ![OpenSpec](https://img.shields.io/badge/OpenSpec-specs-orange) TDD: tests before implementation

> "Taskline is a tiny task board API built on the ANVIL line: spec first, red tests, then the smallest implementation that turns them green."

## What it is
Taskline is the worked example for the ANVIL software factory. It is a framework free task board API on the Python standard library only: create a task, list tasks, complete a task, with persistence to a JSON file. It exists to show the factory trail, not to be a production service. There is no auth, by design, for this local scope.

## How it was built on the line
This was a build from zero: no code existed when the work order was written, and this repo is the trail the factory left (work order, spec, tests first, red and green evidence, reviews, run report). The factory run recorded here used the sdlc-default pipeline. ANVIL also ships a dedicated greenfield pipeline for starting from an idea, with a blueprint station and project scaffolding in front of the same line.

1. Intake: work-orders/wo-taskline-001.json, a feature work order with no risk hints.
2. Spec: .openspec/specs/taskline-api/spec.md, Status approved, with scenarios S1 to S6.
3. Tests first: tests/test_taskline.py, one named test per scenario.
4. Red evidence: the tests were run before any implementation existed. See [evidence/red.txt](evidence/red.txt).
5. Build: taskline/store.py holds persistence and validation, taskline/api.py maps outcomes to status codes.
6. Green evidence: the same tests pass after the build. See [evidence/green.txt](evidence/green.txt).
7. Reviews: four review files under reviews/taskline-api/, one per reviewer station, all passing with honest findings.
8. Run: the ANVIL runner produced runs/wo-taskline-001/report.json, with a packet per agent station, envelopes and a swimlane.
9. Gates: `anvil check . --slug taskline-api` passes the spec, TDD and review gates.

## Quick start
```bash
python3 -m unittest discover -s tests -v
```

## Contributing
Every change starts with a spec under .openspec/specs/ (OpenSpec). Update the spec and its scenario tests before changing the implementation.

## Documentation

| Document | What it covers |
|---|---|
| [.openspec/specs/taskline-api/spec.md](.openspec/specs/taskline-api/spec.md) | The Taskline API spec, scenarios S1 to S6 |
| [evidence/red.txt](evidence/red.txt) | Test output before the implementation existed |
| [evidence/green.txt](evidence/green.txt) | Test output after the implementation |
| [runs/wo-taskline-001/report.json](runs/wo-taskline-001/report.json) | The ANVIL run report for this work order |

## License

[Apache 2.0](LICENSE)

---

## Developer

Eduardo Arana

## Support this with a ko-fi

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H51MPWG)
