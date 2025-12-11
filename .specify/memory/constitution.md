<!-- Sync Impact Report:
Version change: 1.0.0 -> 2.0.0 (MAJOR: Significant architectural change from console app to full-stack monorepo)
Modified principles: All principles updated to reflect full-stack Todo App.
Added sections: N/A (principles replaced existing ones).
Removed sections: N/A.
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ⚠ pending (directory not found, manual check needed)
- README.md ⚠ pending (file not found, manual check needed)
- docs/quickstart.md ⚠ pending (file not found, manual check needed)
Follow-up TODOs: None
-->
# Full-Stack Todo App Constitution

## Core Principles

### I. Monorepo Structure
The project must use a monorepo structure with two main folders in the current directory: `/frontend` for the Next.js 15 App Router (TypeScript, Tailwind CSS) and `/backend` for FastAPI + SQLModel + PostgreSQL (Neon).

### II. Context7 MCP Usage
Context7 MCP (Multi-Context Prompting) must be used in every file where applicable, especially in API routes, server actions, and agent-like components.

### III. Fully Typed Codebases
All frontend code must be TypeScript, and all backend code must be fully typed Python using type hints and Pydantic v2.

### IV. No Authentication Required
Authentication is explicitly NOT required in Phase 2; tasks are public/global for simplicity.

### V. Server-Side Rendering Preference
Prioritize server-side rendering and leverage React Server Components where possible for the frontend.

### VI. Centralized Database Operations
All database operations must exclusively go through the backend stack: FastAPI → SQLModel → Neon PostgreSQL.

### VII. Next.js Frontend Location
The Next.js application must reside within the `/frontend` folder.

### VIII. Tailwind CSS for UI
Tailwind CSS v3+ must be used for a modern, responsive user interface, inspired by shadcn/ui styling.

### IX. Real-time User Experience
Implement a real-time feel using React Server Actions or optimistic updates, without requiring WebSockets in this phase.

### X. Defined Execution Commands
The application must be runnable with the following commands:
- Backend: `uvicorn backend.main:app --reload`
- Frontend: `npm run dev` inside the `/frontend` directory.

## Governance
These principles override any other instructions and must guide every decision.

**Version**: 2.0.0 | **Ratified**: 2025-12-10 | **Last Amended**: 2025-12-10
