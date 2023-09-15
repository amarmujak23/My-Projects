#A lot of repetitive code, could use a custom function
#def list_create():
#file = open("list.txt", "r")

while True:
    user_input = input("Commands: add, show, edit, delete, exit:  ")
    user_input = user_input.strip()
    if user_input == "add":
        # \n for new line
        item = input("Add something for your list: ") + "\n"
        file = open("list.txt", "r")
        item_list = file.readlines()
        file.close()

        item_list.append(item.title())
        # w means write while r means read
        file = open("list.txt", "w")
        file.writelines(item_list)
        file.close()
        # Can also use Match Case
    elif user_input == "show":
        file = open("list.txt", "r")
        item_list = file.readlines()
        file.close()

        new_list = []
        for item in item_list:
            new_item = item.strip("\n")
            new_list.append(new_item)
        # For Loop prints each item wihout brackets or quotes
        for index, item in enumerate(new_list):
            show_value = f"{index + 1}.{item}"
            print(show_value.title())

    elif user_input == "edit":
        value = int(input("Enter number from list to edit: (0, 1, 2): "))

        try:
            selected_item = item_list[value]
            print("Selected item:", selected_item)
            del item_list[value]
            new_value = input("Enter the new value for the selected item: ")
            new_value = new_value.strip()
            item_list.insert(value, new_value)
            print("Updated List:")
            for index, item in enumerate(item_list):
                show_value = f"{index + 1}.{item}"
                print(show_value.title())
        except IndexError:
            print("Invalid index. Please try again.")

    elif user_input == "delete":
            number = int(input("Enter number from list to delete: (1, 2, 3): "))
            item_list.pop(number - 1)

    elif user_input == "exit":
        print("Bye!")
        break

    else:
        print("Unknown Command")