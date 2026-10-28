# Taskline API

Status: approved
Slug: taskline-api

## Roles
- implementer: builds the change described here
- reviewer: checks the change against this spec
- qa: checks the scenarios below with tests
- product_owner: owns the purpose and accepts the result

## Purpose
Taskline is a tiny task board API for a single local user. It creates tasks, lists them, and marks them done, with storage in a JSON file.

## Requirements
- Creating a task with a title returns 201 with an id and status open.
- Listing returns every created task.
- Completing a task marks it done; completing a missing task returns 404.
- Creating a task without a title returns 400.
- Tasks persist to a JSON file and survive a reload.

## Scenarios

### Scenario: Create a task
- S1: Given no tasks, when a task is created with a title, then the response is 201 with an id and status open.

### Scenario: List tasks
- S2: Given two created tasks, when tasks are listed, then both are returned.

### Scenario: Complete a task
- S3: Given a created task, when it is completed, then its status is done.

### Scenario: Complete a missing task
- S4: Given no task with that id, when completion is requested, then the response is 404.

### Scenario: Create without a title
- S5: Given a create request with no title, when it is handled, then the response is 400.

### Scenario: Persistence across reload
- S6: Given a task stored in a JSON file, when a new store loads the same file, then the task is still there.
