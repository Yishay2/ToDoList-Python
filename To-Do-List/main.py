import sys


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):

        print("____ Add Task ____")
        title = input("Title: ")
        description = input("Description: ")
        completed = False
        self.tasks.append([title, description, completed])
        to_exit = input("Do you want to add more tasks: Enter y for yes or q to quit.. ").lower()
        while to_exit != "y" and to_exit != "q":
            to_exit = input("Do you want to add more tasks: Enter y for yes or q to quit.. ").lower()
        if to_exit == "y":
            self.add_task()
        elif to_exit == "q":
            return

    def display_tasks(self):
        if len(self.tasks):
            for i, task in enumerate(self.tasks):
                if isinstance(task, (list, tuple)) and len(task) >= 3:
                    print(f"{i+1}:\n"
                          f"Title: {task[0]}\n"
                          f"Description: {task[1]}\n"
                          f"Status: {"Completed" if task[2] else "Not completed"}\n")
        else:
            print("You don't have missions yet...")

    def complete_tasks(self):
        self.display_tasks()
        if not self.tasks:
            print("You don't have tasks yet..")
            return

        complete_mission = input("What mission do you want to complete? Enter a number or q to quit: ")
        while not complete_mission.isdigit() or int(complete_mission) <= 0 or int(complete_mission) > len(self.tasks):
            if complete_mission == "q":
                print("OK! You are out!")
                return
            if not complete_mission.isdigit():
                print("You have to insert a number!")
            else:
                print(f"You don't have mission number {complete_mission}")
            complete_mission = input("What mission do you want to complete? Enter a number or q to quit: ")

        if not self.tasks[int(complete_mission)-1][2]:
            self.tasks[int(complete_mission)-1] = True
            print("Completed!")
        else:
            print("That mission is already completed!")

        if (False in task for task in self.tasks):
            to_exit = input("Do you want to complete another mission: enter y for yes or q to quit").lower()
            while to_exit != "q" and to_exit != "y":
                to_exit = input("Do you want to complete another mission: enter y for yes or q to quit").lower()
            if to_exit == "y":
                self.complete_tasks()
            elif to_exit == "q":
                return
        else:
            return

    def delete_task(self):
        self.display_tasks()
        remove_mission = input("What mission do you want to remove? Enter a number or q to quit: ")
        while not remove_mission.isdigit() or int(remove_mission) <= 0 or int(remove_mission) >= len(
                self.tasks) + 1:
            if remove_mission == "q":
                print("OK! You are out!")
                break
            if not remove_mission.isdigit():
                print("You have to insert a number!")
            else:
                print(f"You don't have mission number {remove_mission}")
            remove_mission = input("What mission do you want to remove? Enter a number or q to quit: ")

        self.tasks.pop(int(remove_mission) - 1)
        print("Task removed")
        if len(self.tasks):
            to_exit = input("Do you want to remove another mission: enter y for yes or q to quit")
            while to_exit != "q" and to_exit != "y":
                to_exit = input("Do you want to remove another mission: enter y for yes or q to quit")
            if to_exit == "y":
                self.delete_task()
            elif to_exit == "q":
                return
        else:
            return


def main():

    missions = ToDoList()

    while True:
        print(f"1: Add Tasks\n"
              f"2: Display Tasks\n"
              f"3: Complete Tasks\n"
              f"4: Remove Tasks\n"
              f"5: Exit\n")
        user_choice = input("Please enter your choice:")
        while not user_choice.isdigit() or int(user_choice) <= 0 or int(user_choice) > 5:
            user_choice = input("Please enter your choice: ")
        match user_choice:
            case "1":
                missions.add_task()
            case "2":
                missions.display_tasks()
            case "3":
                missions.complete_tasks()
            case "4":
                missions.delete_task()
            case "5":
                sys.exit()


if __name__ == '__main__':
    main()
