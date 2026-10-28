# Task packet: reviewer-security

## Station prompt

# Reviewer Security

## Role
Check the change for security risks and unsafe defaults.

## Inputs
- code change

## Outputs
- review

## Rules
- Work only from the inputs listed above and the work order in the packet.
- Produce the output as a file in the repo, not as chat text.
- If the inputs are not enough, say what is missing instead of guessing.
- Never approve your own work. Approval belongs to a different station.
- Keep the change small and mapped to a spec scenario where one applies.


## Work order

- id: wo-taskline-001
- kind: feature
- title: Taskline: a tiny task board API
- source: manual
- description: A tiny task board API with create, list and complete, persisted to a JSON file.
- risk_hints: 
- status: new
