# Task packet: builder

## Station prompt

# Builder

## Role
Implement the spec so the scenario tests pass.

## Inputs
- spec
- tests

## Outputs
- code change

## Rules
- Work only from the inputs listed above and the work order in the packet.
- Produce the output as a file in the repo, not as chat text.
- If the inputs are not enough, say what is missing instead of guessing.
- Never approve your own work. Approval belongs to a different station.
- Keep the change small and mapped to a spec scenario where one applies.


## Work order

- id: wo-gh-3
- kind: bug
- title: Test coverage gap: S5 empty and whitespace titles not covered through the API
- source: github-issue
- description: Spec S5 in .openspec/specs/taskline-api/spec.md says creating a task without a title returns 400.

Verified behavior of the implementation: the API returns 400 for an empty title and for a whitespace only title. That part honors the spec.

The gap is in the test code: tests/test_taskline.py test_s5_create_without_title_returns_400 covers only a missing title key through the API, and covers the empty string only at the store level (store.add). Nothing exercises an empty or whitespace title through the API itself, so an API regression on those inputs would pass the suite unnoticed.

Suggested fix: extend test_s5 (or add a test) to post empty and whitespace titles through handle() and assert 400 for both. No implementation change is expected.

Note: this is the third copy of this issue. Issues 1 and 2 were opened while bringing up the ANVIL issue workflow itself (their runs exposed a label timing issue and a label parsing bug in the workflow, both fixed). This is the canonical copy for the test gap.

GitHub issue: https://github.com/arananet/anvil-example-taskline/issues/3
- risk_hints: 
- status: new

## Upstream steps

- intake: completed
