from task import TaskManager

def menu():
    manager = TaskManager()
    
    while True:
        print("#" * 10, "TASK MANAGER", "#" *10)
        print("1 - Add Task")
        print("2 - List Task")
        print("3 - Conclude Task")
        print("4 - Remove Task")
        print("5 - Exit")
        
        choice = input("Choose an option: ")
        
if __name__ == "__main__":
    menu()