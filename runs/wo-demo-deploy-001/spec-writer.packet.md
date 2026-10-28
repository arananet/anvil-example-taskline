# Task packet: spec-writer

## Station prompt

# Spec Writer

## Role
Write or revise an OpenSpec spec from a work order.

## Inputs
- work order
- brain

## Outputs
- spec

## Rules
- Work only from the inputs listed above and the work order in the packet.
- Produce the output as a file in the repo, not as chat text.
- If the inputs are not enough, say what is missing instead of guessing.
- Never approve your own work. Approval belongs to a different station.
- Keep the change small and mapped to a spec scenario where one applies.


## Work order

- id: wo-demo-deploy-001
- kind: feature
- title: Demonstrate automatic deploy and post deploy verification
- source: manual
- description: End to end demonstration run for ANVIL execute mode on Taskline: the demonstration executor answers every station packet, reviewers return pass reviews, the approver approves from those run produced reviews, the deployer copies the package into deploy/wo-demo-deploy-001, and the verification gate runs the project test suite against the deployed copy.
- risk_hints: 
- status: new

## Upstream steps

- intake: completed
