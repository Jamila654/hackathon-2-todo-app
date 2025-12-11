# Phase 2 – Full-Stack Todo Web App Specification

## 1. Feature Description

Build a beautiful, fast, full-stack Todo application with exactly the same features as Phase 1, but now on the web. The application must feel modern, smooth, and instantly responsive. Users should never see loading spinners longer than 300ms thanks to server actions and optimistic UI. This is the production version of the console app — now usable by anyone with a browser.

## 2. In-Scope Features

The application will include the following features:
1.  **Add Task**: Users can add new tasks to their todo list.
2.  **Delete Task**: Users can remove existing tasks from their todo list.
3.  **Update Task**: Users can modify details of existing tasks.
4.  **View All Tasks**: Users can view all their tasks, presented in beautiful cards/table format.
5.  **Mark as Complete / Incomplete**: Users can toggle the completion status of a task using a checkbox.
6.  **Priority (High/Medium/Low)**: Tasks can be assigned a priority level (High, Medium, Low), which will be visually distinct.
7.  **Tags/Categories**: Tasks can have multiple tags/categories, displayed as colored pills.
8.  **Search by keyword**: Users can search for tasks using keywords.
9.  **Filter by status, priority, tags**: Users can filter tasks based on their completion status, priority level, and assigned tags.
10. **Sort by due date, priority, name**: Users can sort their tasks by due date, priority, and task name.
11. **Responsive design**: The application will work perfectly on both mobile and desktop devices.

## 3. Out-of-Scope Features

-   User authentication/authorization (assuming a single user for this phase)
-   Real-time collaboration
-   Offline support
-   Advanced reporting or analytics

## 4. User Scenarios & Testing

### Scenario 1: Task Management
-   **Given** a user is on the Todo application homepage
-   **When** they add a new task with a name, priority, tags, and optional due date
-   **Then** the new task appears in the task list
-   **When** they mark a task as complete
-   **Then** the task's status visually updates to complete
-   **When** they update a task's priority
-   **Then** the task's priority visually updates
-   **When** they delete a task
-   **Then** the task is removed from the list

### Scenario 2: Task Viewing and Organization
-   **Given** a user has multiple tasks with varying statuses, priorities, and tags
-   **When** they filter tasks by "High" priority
-   **Then** only tasks with "High" priority are displayed
-   **When** they search for a keyword present in a task name
-   **Then** only tasks matching the keyword are displayed
-   **When** they sort tasks by "Due Date (ascending)"
-   **Then** tasks are ordered by their due dates, earliest first

## 5. Functional Requirements

-   FR1: The system SHALL allow users to add new tasks with a title, description (optional), due date (optional), priority, and tags.
-   FR2: The system SHALL allow users to delete tasks.
-   FR3: The system SHALL allow users to update any editable field of an existing task.
-   FR4: The system SHALL display all tasks in a clear, organized list or table view.
-   FR5: The system SHALL enable users to mark tasks as complete or incomplete via a UI element (e.g., checkbox).
-   FR6: The system SHALL visually differentiate tasks based on their priority (High, Medium, Low).
-   FR7: The system SHALL display assigned tags as colored pills associated with each task.
-   FR8: The system SHALL provide a search bar to filter tasks by keywords in their title or description.
-   FR9: The system SHALL provide filtering options for task status (complete/incomplete), priority (High/Medium/Low), and tags.
-   FR10: The system SHALL provide sorting options for tasks by due date, priority, and name in ascending or descending order.
-   FR11: The system SHALL provide a calendar picker for selecting due dates (nice to have).
-   FR12: The application SHALL have a responsive design, adapting to various screen sizes (mobile, tablet, desktop).

## 6. Non-Functional Requirements

-   NFR1 (Performance): The application SHALL achieve a perceived load time for task list updates (add, delete, update, filter, sort) of less than 300ms for 95% of user interactions.
-   NFR2 (Responsiveness): The UI SHALL be instantly responsive to user input, with no noticeable lag or loading spinners exceeding 300ms.
-   NFR3 (Reliability): The application SHALL maintain 99.9% uptime.
-   NFR4 (Usability): The application SHALL provide an intuitive and modern user interface.

## 7. Key Entities

### Task
-   `id`: Unique identifier (string)
-   `title`: Task title (string, required)
-   `description`: Task description (string, optional)
-   `status`: "completed" | "in_complete" (enum, default "in_complete")
-   `priority`: "high" | "medium" | "low" (enum, default "medium")
-   `tags`: List of strings (e.g., ["work", "personal"], optional)
-   `dueDate`: Date (optional)
-   `createdAt`: Timestamp (auto-generated)
-   `updatedAt`: Timestamp (auto-generated)

## 8. Assumptions

-   The application will run in a modern web browser environment.
-   A backend API will handle data persistence and business logic.
-   No complex user roles or permissions are required at this stage.
-   The "Phase 1" console app features imply the basic task management logic is well-understood.

## 9. Success Criteria

-   All listed in-scope features are fully implemented and functional.
-   The application's visual design is clean, modern, and aesthetically pleasing.
-   User interactions feel fluid, with updates and transitions happening smoothly.
-   The application is fully usable and visually appealing on common mobile and desktop browser sizes.
-   The task list updates (add, delete, update, filter, sort) are perceived as instant by the user, with no loading indicators visible for more than 300ms.

## 10. Open Questions

-   [NEEDS CLARIFICATION: What specific technologies or frameworks are preferred for the full-stack implementation (e.g., React/Next.js, Node.js/Express, database type)?]
-   [NEEDS CLARIFICATION: Should the due date calendar picker be a hard requirement or remain a "nice to have"?]
