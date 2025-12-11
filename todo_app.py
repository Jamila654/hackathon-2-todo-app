# todo_app.py
# #!/usr/bin/env python3
"""
todo_app.py

Command-line Todo application (in-memory, stdlib only).

Features:
- Add Task (description, optional due date YYYY-MM-DD, priority, tags)
- Delete Task by ID
- Update Task fields
- View Task List (pretty table)
- Toggle Complete / Incomplete
- Priorities: high / medium / low
- Tags: multiple free-form tags (comma-separated)
- Search (keyword in description or tags)
- Filter (completion status, priority, due-date range)
- Sort by due date, priority, or alphabetical
"""

import datetime
from typing import List, Optional, Any
from dataclasses import dataclass, field
import sys

PRIORITY_ORDER = {"high": 3, "medium": 2, "low": 1}
VALID_PRIORITIES = list(PRIORITY_ORDER.keys())


@dataclass
class Task:
    id: int
    description: str
    due_date: Optional[datetime.date] = None
    priority: str = "medium"
    tags: List[str] = field(default_factory=list)
    completed: bool = False
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    def __str__(self) -> str:
        status = "[✓]" if self.completed else "[ ]"
        due = f" (Due: {self.due_date.isoformat()})" if self.due_date else ""
        tags = f" #{' #'.join(self.tags)}" if self.tags else ""
        return f"{status} {self.id}. {self.description}{due} [Priority: {self.priority.capitalize()}]{tags}"


class TodoManager:
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, description: str, due_date: Optional[datetime.date] = None,
                 priority: str = "medium", tags: Optional[List[str]] = None) -> Task:
        if tags is None:
            tags = []
        priority = priority.lower() if priority else "medium"
        if priority not in VALID_PRIORITIES:
            priority = "medium"
        task = Task(id=self.next_id, description=description.strip(), due_date=due_date,
                    priority=priority, tags=[t.strip() for t in tags if t.strip()])
        self.tasks.append(task)
        self.next_id += 1
        return task

    def delete_task(self, task_id: int) -> bool:
        for i, t in enumerate(self.tasks):
            if t.id == task_id:
                del self.tasks[i]
                return True
        return False

    def toggle_complete(self, task_id: int) -> bool:
        t = self.find_task(task_id)
        if t:
            t.completed = not t.completed
            return True
        return False

    def update_task(self, task_id: int, description: Optional[str] = None,
                    due_date: Optional[datetime.date] = None, priority: Optional[str] = None,
                    tags: Optional[List[str]] = None) -> Optional[Task]:
        t = self.find_task(task_id)
        if not t:
            return None
        if description is not None:
            t.description = description.strip()
        if due_date is not None:
            t.due_date = due_date
        if priority is not None:
            p = priority.lower()
            if p in VALID_PRIORITIES:
                t.priority = p
        if tags is not None:
            t.tags = [x.strip() for x in tags if x.strip()]
        return t

    def find_task(self, task_id: int) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def view_tasks(self, tasks: Optional[List[Task]] = None) -> None:
        if tasks is None:
            tasks = self.tasks

        if not tasks:
            print("\nNo tasks found.\n")
            return

        # Compute column widths safely
        id_width = max(max((len(str(t.id)) for t in tasks), default=2), 2)
        status_width = 3  # "[ ]" or "[✓]"
        desc_width = max(max((len(t.description) for t in tasks), default=len("Description")), len("Description"))
        priority_width = max(max((len(t.priority) for t in tasks), default=len("Priority")), len("Priority"))
        due_width = max(max((len(t.due_date.isoformat()) for t in tasks if t.due_date), default=len("Due Date")), len("Due Date"))
        tags_width = max(max((len(', '.join(t.tags)) for t in tasks if t.tags), default=len("Tags")), len("Tags"))

        header_fmt = f" {{:<{id_width}}} {{:<{status_width}}}  {{:<{desc_width}}}  {{:<{priority_width}}}  {{:<{due_width}}}  {{:<{tags_width}}}"
        print()
        print(header_fmt.format("ID", " ", "Description", "Priority", "Due Date", "Tags"))
        print(header_fmt.format("-" * id_width, "-" * status_width, "-" * desc_width, "-" * priority_width, "-" * due_width, "-" * tags_width))

        for t in tasks:
            status = "[✓]" if t.completed else "[ ]"
            due = t.due_date.isoformat() if t.due_date else ""
            tags = ", ".join(t.tags) if t.tags else ""
            print(header_fmt.format(t.id, status, t.description, t.priority.capitalize(), due, tags))
        print()

    def search_tasks(self, keyword: str) -> List[Task]:
        kw = keyword.lower().strip()
        results: List[Task] = []
        for t in self.tasks:
            if kw in t.description.lower():
                results.append(t)
                continue
            for tag in t.tags:
                if kw in tag.lower():
                    results.append(t)
                    break
        return results

    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None,
                     due_from: Optional[datetime.date] = None, due_to: Optional[datetime.date] = None) -> List[Task]:
        results = []
        for t in self.tasks:
            if status is not None:
                if status == "complete" and not t.completed:
                    continue
                if status == "incomplete" and t.completed:
                    continue
            if priority is not None:
                if t.priority != priority:
                    continue
            if due_from is not None:
                if not t.due_date or t.due_date < due_from:
                    continue
            if due_to is not None:
                if not t.due_date or t.due_date > due_to:
                    continue
            results.append(t)
        return results

    def sort_tasks(self, tasks: List[Task], sort_by: str) -> List[Task]:
        if sort_by == "due":
            # Tasks without due date go to the end
            return sorted(tasks, key=lambda x: (x.due_date is None, x.due_date or datetime.date.max, -PRIORITY_ORDER.get(x.priority, 0), x.description.lower()))
        if sort_by == "priority":
            # High -> Low (descending by mapped priority)
            return sorted(tasks, key=lambda x: (-PRIORITY_ORDER.get(x.priority, 0), x.due_date or datetime.date.max, x.description.lower()))
        if sort_by == "alpha":
            return sorted(tasks, key=lambda x: x.description.lower())
        # default: by id (created order)
        return sorted(tasks, key=lambda x: x.id)


# -------- Input helpers --------
def get_valid_date(prompt: str) -> Optional[datetime.date]:
    while True:
        s = input(prompt).strip()
        if not s:
            return None
        try:
            return datetime.datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("  Invalid date. Use YYYY-MM-DD, or leave blank.")


def get_priority(prompt: str, default: Optional[str] = "medium") -> str:
    default = default or "medium"
    while True:
        s = input(f"{prompt} [{'/'.join(VALID_PRIORITIES)}] (default: {default}): ").strip().lower()
        if not s:
            return default
        if s in VALID_PRIORITIES:
            return s
        print(f"  Invalid priority. Choose one of: {', '.join(VALID_PRIORITIES)}.")


def get_tags(prompt: str) -> List[str]:
    s = input(prompt).strip()
    if not s:
        return []
    # split by comma, strip whitespace, remove empty
    return [t.strip() for t in s.split(",") if t.strip()]


def get_int(prompt: str) -> Optional[int]:
    s = input(prompt).strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        print("  Please enter a valid integer.")
        return None


def prompt_yes_no(prompt: str, default: bool = True) -> bool:
    suffix = "Y/n" if default else "y/N"
    s = input(f"{prompt} ({suffix}): ").strip().lower()
    if not s:
        return default
    return s[0] == "y"


# -------- Main CLI --------
def print_banner() -> None:
    print("=" * 60)
    print("   Todo CLI — Fast, simple, terminal-first todo manager")
    print("=" * 60)
    print("Commands: add / view / search / update / delete / toggle / sort / filter / exit")
    print()


def add_task_flow(manager: TodoManager) -> None:
    print("\nAdd Task")
    desc = input(" Description: ").strip()
    if not desc:
        print("  Description cannot be empty. Aborting add.\n")
        return
    due = get_valid_date(" Due date (YYYY-MM-DD) [leave blank for none]: ")
    priority = get_priority(" Priority", default="medium")
    tags = get_tags(" Tags (comma-separated) [optional]: ")
    task = manager.add_task(description=desc, due_date=due, priority=priority, tags=tags)
    print(f"\n  Added: {task}\n")


def view_all_flow(manager: TodoManager, sort_by: Optional[str] = None) -> None:
    tasks = manager.tasks[:]
    if sort_by:
        tasks = manager.sort_tasks(tasks, sort_by)
    manager.view_tasks(tasks)


def search_flow(manager: TodoManager) -> None:
    kw = input("\nEnter search keyword (searches description & tags): ").strip()
    if not kw:
        print("  Empty keyword. Returning to menu.\n")
        return
    results = manager.search_tasks(kw)
    if not results:
        print("  No matching tasks found.\n")
        return
    print(f"\nFound {len(results)} matching task(s):")
    manager.view_tasks(results)


def update_flow(manager: TodoManager) -> None:
    tid = get_int("\nEnter task ID to update: ")
    if tid is None:
        print("  No ID entered. Aborting update.\n")
        return
    t = manager.find_task(tid)
    if not t:
        print(f"  Task with ID {tid} not found.\n")
        return
    print(f"\nUpdating Task {tid}:")
    print(f" Current: {t}\n")
    new_desc = input(" New description [leave blank to keep current]: ").strip()
    new_due = None
    raw = input(" New due date (YYYY-MM-DD) [leave blank to keep current, '-' to clear]: ").strip()
    if raw == "":
        new_due = t.due_date  # keep
    elif raw == "-":
        new_due = None
    else:
        try:
            new_due = datetime.datetime.strptime(raw, "%Y-%m-%d").date()
        except ValueError:
            print("  Invalid date format. Keeping current due date.")
            new_due = t.due_date
    new_priority = input(f" New priority [{'/'.join(VALID_PRIORITIES)}] [leave blank to keep current]: ").strip().lower()
    if new_priority == "":
        new_priority = t.priority
    elif new_priority not in VALID_PRIORITIES:
        print("  Invalid priority entered. Keeping current priority.")
        new_priority = t.priority

    tags_raw = input(" New tags (comma-separated) [leave blank to keep current, '-' to clear]: ").strip()
    if tags_raw == "":
        new_tags = t.tags
    elif tags_raw == "-":
        new_tags = []
    else:
        new_tags = [x.strip() for x in tags_raw.split(",") if x.strip()]

    # Apply updates (only pass changed fields)
    manager.update_task(tid,
                        description=new_desc if new_desc != "" else None,
                        due_date=new_due,
                        priority=new_priority,
                        tags=new_tags)
    print("  Task updated.\n")


def delete_flow(manager: TodoManager) -> None:
    tid = get_int("\nEnter task ID to delete: ")
    if tid is None:
        print("  No ID entered. Aborting delete.\n")
        return
    t = manager.find_task(tid)
    if not t:
        print(f"  Task with ID {tid} not found.\n")
        return
    if not prompt_yes_no(f"Are you sure you want to permanently delete task {tid}?"):
        print("  Delete cancelled.\n")
        return
    if manager.delete_task(tid):
        print("  Task deleted.\n")
    else:
        print("  Failed to delete task — not found.\n")


def toggle_flow(manager: TodoManager) -> None:
    tid = get_int("\nEnter task ID to toggle complete/incomplete: ")
    if tid is None:
        print("  No ID entered. Aborting.\n")
        return
    if manager.toggle_complete(tid):
        t = manager.find_task(tid)
        print(f"  Toggled. Now: {'Complete' if t and t.completed else 'Incomplete'}\n")
    else:
        print("  Task not found.\n")


def sort_flow(manager: TodoManager) -> None:
    print("\nSort Options:\n  1) Due date (earliest first)\n  2) Priority (High -> Low)\n  3) Alphabetical (by description)\n")
    choice = input("Choose sort (1/2/3): ").strip()
    mapping = {"1": "due", "2": "priority", "3": "alpha"}
    sort_by = mapping.get(choice)
    if not sort_by:
        print("  Invalid choice. Returning to menu.\n")
        return
    tasks = manager.sort_tasks(manager.tasks, sort_by)
    manager.view_tasks(tasks)


def filter_flow(manager: TodoManager) -> None:
    print("\nFilter by completion status, priority, and/or due date range.")
    stat = input(" Status (complete/incomplete/any) [any]: ").strip().lower()
    if stat not in ("complete", "incomplete", "any", ""):
        print("  Invalid status. Using 'any'.")
        stat = "any"
    status = None if stat in ("any", "") else stat

    pr = input(f" Priority ({'/'.join(VALID_PRIORITIES)}/any) [any]: ").strip().lower()
    if pr not in VALID_PRIORITIES + ["any", ""]:
        print("  Invalid priority. Using 'any'.")
        pr = "any"
    priority = None if pr in ("any", "") else pr

    print(" Due date range (leave blank to skip). Provide dates in YYYY-MM-DD.")
    due_from = get_valid_date("  From (inclusive): ")
    due_to = get_valid_date("  To (inclusive): ")

    results = manager.filter_tasks(status=status, priority=priority, due_from=due_from, due_to=due_to)
    if not results:
        print("\n  No tasks match the filter criteria.\n")
        return
    # Ask for optional sorting
    if prompt_yes_no("Sort results? (by due date recommended)", default=True):
        print("Sort by: 1) due  2) priority  3) alpha")
        s = input("Choose sort (1/2/3 or leave blank for id): ").strip()
        mapping = {"1": "due", "2": "priority", "3": "alpha"}
        sort_by = mapping.get(s)
        if sort_by:
            results = manager.sort_tasks(results, sort_by)
    manager.view_tasks(results)


def main_loop() -> None:
    manager = TodoManager()
    print_banner()

    # Seed demo tasks (optional) - commented out; uncomment for quick testing
    # manager.add_task("Buy groceries", due_date=datetime.date.today() + datetime.timedelta(days=1), priority="high", tags=["errands", "home"])
    # manager.add_task("Finish report", due_date=datetime.date.today() + datetime.timedelta(days=3), priority="high", tags=["work"])

    while True:
        print("Menu:")
        print(" 1) Add task")
        print(" 2) View all tasks")
        print(" 3) Search tasks")
        print(" 4) Update task")
        print(" 5) Delete task")
        print(" 6) Toggle complete")
        print(" 7) Sort tasks")
        print(" 8) Filter tasks")
        print(" 9) Help")
        print(" 0) Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            add_task_flow(manager)
        elif choice == "2":
            view_all_flow(manager)
        elif choice == "3":
            search_flow(manager)
        elif choice == "4":
            update_flow(manager)
        elif choice == "5":
            delete_flow(manager)
        elif choice == "6":
            toggle_flow(manager)
        elif choice == "7":
            sort_flow(manager)
        elif choice == "8":
            filter_flow(manager)
        elif choice == "9":
            print_banner()
        elif choice == "0":
            print("\nGoodbye — tasks are stored in memory only and will be lost on exit.")
            break
        else:
            print("Invalid option. Enter a number from the menu.\n")


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Exiting.")
        sys.exit(0)


