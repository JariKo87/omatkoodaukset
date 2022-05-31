import os
import sys
command_list = {
    "quit": "finnish program",
    "clear": "clear console",
    "update": "update storage's memory",
    "check": "check items on storage.",
    "clear_memory": "clear storage's memory",
}


class Storage:
    def __init__(self):
        self.__products_and_pcs = []

    def start(self):
        self.add_on_list()
        while True:
            command = input("Give a command. (commands to see all commands): ").lower()
            if command == "quit":
                break
            elif command == "clear":
                self.clear_console()
            elif command == "commands":
                for command in command_list:
                    print(f"{command} : {command_list[command]}")
            elif command == "check":
                for item in self.__products_and_pcs:
                    print(f"{item}.")
            elif command == "clear_memory":
                self.clear_memory()
            elif  command == "update":
                self.update_memory()
            else:
                print("unknown command!")

    def clear_console(self):
        os.system("cls")

    def add_on_list(self):
        file = open("storage_memory.txt", "r")
        for item in file:
            item = item.split(";")
            item[1] = item[1].replace("\n", "")
            self.__products_and_pcs.append(f"{item[0]}, {item[1]} pcs")

    def clear_memory(self):
        file = open("storage_memory.txt", "r+")
        file.truncate(0)
        file.close()

    def update_memory(self):
        file = open("storage_memory.txt", "r+")
        update_or_add_new_item  = input("Do you want to update item or add new? (u-update, n-new item): ")
        if update_or_add_new_item == "n":
            item_and_pcs = input("Please give a item and how many pcs. (in format t-shirt 3)").split(" ")
            file.write(f"{item_and_pcs[0]};{item_and_pcs[1]}")
        elif  update_or_add_new_item == "u":
            item = input("Item which you want to update and pcs. (t-shirt 3): ").split(" ")
            for saved_item in file:
                print(saved_item)
                if saved_item.split(";")[0] == item[0]:
                    sys.stdout.write(saved_item.replace(saved_item.split(";")[1], item[1]))
        file.close()


if __name__ == "__main__":
    Storage().clear_console()
    Storage().start()
