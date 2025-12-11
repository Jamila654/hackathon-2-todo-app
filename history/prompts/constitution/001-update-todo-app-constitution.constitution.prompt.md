---
id: 001
title: Update Todo App Constitution
stage: constitution
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-physical-ai-book
user: user
command: /sp.constitution
labels: [constitution, documentation, update]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
tests:

---

## Prompt

# Project Constitution - Governing Principles

You are building a Todo console application in Python. Before writing any code, internalize and strictly follow these unbreakable rules for the entire project:

- This is a pure in-memory Python console app — no files, no databases, no external libraries beyond the Python standard library.
- Code must be clean, PEP 8 compliant, well-commented, and highly readable.
- Use meaningful variable and function names.
- Prioritize simplicity, clarity, and user experience in the console interface.
- Every user interaction must include clear prompts, helpful error messages, and confirmation feedback.
- Implement robust input validation — never let invalid input crash the program.
- The app must run in an infinite loop with a numbered menu until the user chooses to exit.
- All features listed in specify.md must be implemented exactly — no more, no less.
- Use classes and proper separation of concerns (Task class + TodoManager).
- Include a short in-code usage guide or welcome message.
- The final deliverable must be a single, runnable Python script called `todo_app.py`.

These principles override any other instructions and must guide every decision.

## Response snapshot

Updated the project constitution at `.specify/memory/constitution.md` with new core principles for a Python Todo console application. Performed consistency checks on related templates and generated a Sync Impact Report. Marked templates requiring manual follow-up due to missing files/directories.

## Outcome

- ✅ Impact: Successfully updated project constitution with user-defined principles.
- 🧪 Tests: N/A
- 📁 Files: Updated constitution, checked related templates.
- 🔁 Next prompts: Proceed with further project development based on the updated constitution.
- 🧠 Reflection: Encountered issues with PHR script and missing command/documentation files, requiring manual PHR creation and adjustment of consistency report.

## Evaluation notes (flywheel)

- Failure modes observed: PHR creation script failed due to missing template; command and documentation files were not found for consistency checks.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Investigate standard location/access method for command and documentation files in this environment to improve consistency checks.
