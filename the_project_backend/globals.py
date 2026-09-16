

def add_todo(r : str):
    with open('todos.txt', 'a') as todohandle:
        todohandle.write("\n" + r)

    
def get_todos() -> str:
    with open('todos.txt', 'r') as todohandle:
        return todohandle.read().splitlines()