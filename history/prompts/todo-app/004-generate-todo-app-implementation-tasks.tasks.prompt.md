---
id: 004
title: Generate Todo App Implementation Tasks
stage: tasks
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20251101
feature: todo-app
branch: 001-todo-app
user: user
command: /sp.tasks
labels: [tasks, todo-app]
links:
  spec: /Users/jamilayaqoobdhedhi/specs/001-todo-app/spec.md
  plan: /Users/jamilayaqoobdhedhi/specs/001-todo-app/plan.md
  tasks: /Users/jamilayaqoobdhedhi/specs/001-todo-app/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - /Users/jamilayaqoobdhedhi/specs/001-todo-app/tasks.md
tests:

---

## Prompt

# Implementation Task List

Implement in this exact order:

1. Import necessary modules (`datetime`, `typing` if desired)
2. Define the `Task` dataclass or class with all required attributes
3. Implement `__str__` or a `display()` method for pretty printing
4. Create `TodoManager` class with:
   - `__init__`: empty task list + next_id = 1
   - `add_task()`
   - `delete_task(task_id)`
   - `update_task(task_id)`
   - `toggle_complete(task_id)`
   - `view_tasks(sort_by=None, filter_criteria=None, search_term=None)`
   - `search_and_filter()` helper
   - `list_tasks()` with sorting and filtering applied
5. Implement input helpers:
   - get valid priority
   - get valid date (or None)
   - get tags (comma-separated)
6. Build main menu loop with options:
   1. Add task
   2. View all tasks
   3. Search tasks
   4. Update task
   5. Delete task
   6. Toggle complete
   7. Sort tasks (sub-menu)
   8. Exit
7. Add welcome banner and short help text
8. Ensure graceful handling of empty list and invalid IDs
9. Test all paths mentally and fix any obvious bugs
10. Final polish: consistent formatting, colors optional but not required

Deliver the complete, runnable script as `todo_app.py`

## Response snapshot

Generated the `tasks.md` file for the Todo Application, detailing implementation steps organized by user story and phase. The task list ensures a structured approach to development.

## Outcome

- ✅ Impact: Successfully created a detailed and ordered task list for the Todo application.
- 🧪 Tests: N/A
- 📁 Files: Generated `/Users/jamilayaqoobdhedhi/specs/001-todo-app/tasks.md`.
- 🔁 Next prompts: User can now proceed with implementing the tasks.
- 🧠 Reflection: The `check-prerequisites.sh` script returned an incorrect feature directory initially, which required careful manual path management during task generation.

## Evaluation notes (flywheel)

- Failure modes observed: `check-prerequisites.sh` provided incorrect `FEATURE_DIR`.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Fix `check-prerequisites.sh` to correctly identify the active feature branch.
