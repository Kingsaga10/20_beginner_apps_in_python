todos = list()
while True:
    user_input = input("enter add, show, edit, or exit: ").lower()

    match user_input.strip():
        case 'add':
            todo = input("Add todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            for index, item in enumerate(todos, start=1):
                print(f'{index} -> {item}')
            edit = int(input("enter the index of the item to edit: "))
            if edit in range(1, len(todos)):
                todos[edit] = input(f'edit {todos[edit]} here: ')
            else:
                print("print index not found")
        case 'exit':
            print("closing App")
            break
print("Bye!")
