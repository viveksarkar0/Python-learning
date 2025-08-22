# ===============================
# ✅ TODO LIST APPLICATION
# ===============================

import json
import os
from datetime import datetime

class TodoList:
    """A simple todo list application"""
    
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    return json.load(file)
            return []
        except Exception as e:
            print(f"Error loading todos: {e}")
            return []
    
    def save_todos(self):
        """Save todos to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.todos, file, indent=2)
        except Exception as e:
            print(f"Error saving todos: {e}")
    
    def add_todo(self, title, description="", priority="medium"):
        """Add a new todo item"""
        todo = {
            "id": len(self.todos) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_at": None
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✅ Todo added: {title}")
    
    def list_todos(self, show_completed=True):
        """List all todos"""
        if not self.todos:
            print("📝 No todos found!")
            return
        
        print("\n📋 TODO LIST:")
        print("=" * 60)
        
        for todo in self.todos:
            if not show_completed and todo["completed"]:
                continue
            
            status = "✅" if todo["completed"] else "⏳"
            priority_icon = {
                "high": "🔴",
                "medium": "🟡", 
                "low": "🟢"
            }.get(todo["priority"], "⚪")
            
            print(f"{status} {priority_icon} [{todo['id']}] {todo['title']}")
            if todo["description"]:
                print(f"    📄 {todo['description']}")
            print(f"    📅 Created: {todo['created_at']}")
            
            if todo["completed"] and todo["completed_at"]:
                print(f"    ✅ Completed: {todo['completed_at']}")
            
            print()
    
    def complete_todo(self, todo_id):
        """Mark a todo as completed"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                if todo["completed"]:
                    print(f"❌ Todo {todo_id} is already completed!")
                else:
                    todo["completed"] = True
                    todo["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.save_todos()
                    print(f"✅ Todo completed: {todo['title']}")
                return
        
        print(f"❌ Todo with ID {todo_id} not found!")
    
    def delete_todo(self, todo_id):
        """Delete a todo item"""
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                deleted_todo = self.todos.pop(i)
                self.save_todos()
                print(f"🗑️ Todo deleted: {deleted_todo['title']}")
                return
        
        print(f"❌ Todo with ID {todo_id} not found!")
    
    def edit_todo(self, todo_id, title=None, description=None, priority=None):
        """Edit a todo item"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                if title:
                    todo["title"] = title
                if description:
                    todo["description"] = description
                if priority:
                    todo["priority"] = priority
                
                self.save_todos()
                print(f"✏️ Todo updated: {todo['title']}")
                return
        
        print(f"❌ Todo with ID {todo_id} not found!")
    
    def search_todos(self, keyword):
        """Search todos by keyword"""
        results = []
        keyword = keyword.lower()
        
        for todo in self.todos:
            if (keyword in todo["title"].lower() or 
                keyword in todo["description"].lower()):
                results.append(todo)
        
        if results:
            print(f"\n🔍 Search results for '{keyword}':")
            print("=" * 60)
            for todo in results:
                status = "✅" if todo["completed"] else "⏳"
                print(f"{status} [{todo['id']}] {todo['title']}")
                if todo["description"]:
                    print(f"    📄 {todo['description']}")
                print()
        else:
            print(f"🔍 No todos found matching '{keyword}'")
    
    def get_stats(self):
        """Get todo statistics"""
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo["completed"])
        pending = total - completed
        
        print("\n📊 TODO STATISTICS:")
        print("=" * 30)
        print(f"📝 Total todos: {total}")
        print(f"✅ Completed: {completed}")
        print(f"⏳ Pending: {pending}")
        
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"📈 Completion rate: {completion_rate:.1f}%")
        
        # Priority breakdown
        priorities = {}
        for todo in self.todos:
            priority = todo["priority"]
            priorities[priority] = priorities.get(priority, 0) + 1
        
        if priorities:
            print("\n🎯 Priority breakdown:")
            for priority, count in priorities.items():
                print(f"   {priority.capitalize()}: {count}")

def main_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("🎯 TODO LIST APPLICATION")
    print("=" * 50)
    print("1. 📝 Add new todo")
    print("2. 📋 List all todos")
    print("3. ✅ Complete todo")
    print("4. 🗑️ Delete todo")
    print("5. ✏️ Edit todo")
    print("6. 🔍 Search todos")
    print("7. 📊 Show statistics")
    print("8. 💾 Save todos")
    print("9. 🚪 Exit")
    print("=" * 50)

def get_user_input(prompt, required=True):
    """Get user input with validation"""
    while True:
        user_input = input(prompt).strip()
        if user_input or not required:
            return user_input
        print("❌ This field is required!")

def main():
    """Main application loop"""
    todo_list = TodoList()
    
    print("🎉 Welcome to the Todo List Application!")
    
    while True:
        main_menu()
        choice = get_user_input("Enter your choice (1-9): ")
        
        if choice == "1":
            # Add new todo
            title = get_user_input("Enter todo title: ")
            description = get_user_input("Enter description (optional): ", required=False)
            
            print("\nPriority levels:")
            print("1. 🔴 High")
            print("2. 🟡 Medium")
            print("3. 🟢 Low")
            priority_choice = get_user_input("Enter priority (1-3, default=2): ", required=False)
            
            priority_map = {"1": "high", "2": "medium", "3": "low"}
            priority = priority_map.get(priority_choice, "medium")
            
            todo_list.add_todo(title, description, priority)
        
        elif choice == "2":
            # List todos
            show_completed = get_user_input("Show completed todos? (y/n, default=y): ", required=False).lower() != "n"
            todo_list.list_todos(show_completed)
        
        elif choice == "3":
            # Complete todo
            todo_list.list_todos(show_completed=False)
            todo_id = get_user_input("Enter todo ID to complete: ")
            try:
                todo_list.complete_todo(int(todo_id))
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "4":
            # Delete todo
            todo_list.list_todos()
            todo_id = get_user_input("Enter todo ID to delete: ")
            try:
                todo_list.delete_todo(int(todo_id))
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "5":
            # Edit todo
            todo_list.list_todos()
            todo_id = get_user_input("Enter todo ID to edit: ")
            try:
                todo_id = int(todo_id)
                title = get_user_input("Enter new title (press Enter to skip): ", required=False)
                description = get_user_input("Enter new description (press Enter to skip): ", required=False)
                
                print("\nPriority levels:")
                print("1. 🔴 High")
                print("2. 🟡 Medium") 
                print("3. 🟢 Low")
                priority_choice = get_user_input("Enter new priority (1-3, press Enter to skip): ", required=False)
                
                priority_map = {"1": "high", "2": "medium", "3": "low"}
                priority = priority_map.get(priority_choice) if priority_choice else None
                
                todo_list.edit_todo(todo_id, title, description, priority)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "6":
            # Search todos
            keyword = get_user_input("Enter search keyword: ")
            todo_list.search_todos(keyword)
        
        elif choice == "7":
            # Show statistics
            todo_list.get_stats()
        
        elif choice == "8":
            # Save todos
            todo_list.save_todos()
            print("💾 Todos saved successfully!")
        
        elif choice == "9":
            # Exit
            print("👋 Thank you for using the Todo List Application!")
            print("💾 Your todos have been saved automatically.")
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 1-9.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
