class Task :

    def __init__(self,description):
        self.description=description
        self.completed=False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.description} [{status}]"


class ToDoList :
    def __init__(self):
        self.tasks=[]


    def displaymenu(self):
        print("To Do List Menu :")
        print("1. Add Task")
        print("2. View Task")
        print("3. Update Task")
        print("4.Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit\n")

    def addtask(self):
        description = input("Enter the Task Description: ")
        newtask = Task(description)
        self.tasks.append(newtask)
        print("Task Added Successfully!\n")

    def viewtask(self):
        if len(self.tasks) == 0:
            print("No Tasks Available.\n")
        else:
            print("Your To-Do List:")
            index = 1
            for task in self.tasks:
                status = "✓" if task.completed else "✗"
                print(str(index) + ". " + task.description + " [" + status + "]")  # Concatenation instead of f-string
                index += 1
            print()

    def updatetask(self):
        self.viewtask()

        if self.tasks :
            tasknumber = int(input("Enter the task number to update :"))

            if 1 <= tasknumber <= len(self.tasks) :
                newdescription = input("Enter the new description to update :")
                self.tasks[tasknumber - 1].description=newdescription
                print("Task updated successfully!\n")

            else :
                print("Invalid Task number please enter valid number !\n")



    def deletetask(self):
        self.viewtask()

        if self.tasks :
            tasknumber=int(input("Enter the task number to delete :"))

            if 1 <= tasknumber <=  len(self.tasks) :
                removedtasks=self.tasks.pop(tasknumber - 1)
                print("Tasks deleted successfully !")
            else :
                print("Invalid Task number please enter valid tasks number !")


    def marktaskascompleted(self):
        self.viewtask()

        if self.tasks:
            tasknumber = int(input("Enter the task number to mark as completed :"))

            if 1 <= tasknumber <= len(self.tasks):
                self.tasks[tasknumber - 1].completed = True
                print("Task marked as completed!\n")
            else:
                print("Invalid Task number please enter valid tasks number !")





def main():
    todo_list=ToDoList()

    while True :
        todo_list.displaymenu()

        choice=input("Enter Your Choice :")

        if choice == '1':
            todo_list.addtask()

        elif choice == '2':
                todo_list.viewtask()

        elif choice == '3':
            todo_list.updatetask()

        elif choice == '4':
            todo_list.deletetask()

        elif choice == '5':
            todo_list.marktaskascompleted()

        elif choice == '6':
            print("Exiting ToDo List !!")
            break
        else :
            print("Invalid choice please enter valid choice !")


if __name__ == "__main__":
    main()


