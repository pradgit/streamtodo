FILEPATH = 'todos.txt'

#Added comment for reqcycle1
def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(newtodo,filepath=FILEPATH):
    with open(filepath,'w') as file_write:
        file_write.writelines(newtodo)

def newlogichere():
    pass


