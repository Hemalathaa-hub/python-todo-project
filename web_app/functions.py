FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath,"r") as file_local: #content manager of read file
        todos_local=file_local.readlines()
    return todos_local
        
def write_todos(todo,filepath=FILEPATH):
    with open(filepath,"w") as file_local: #content manager of read file
            file_local.writelines(todo)

