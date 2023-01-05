FILEPATH = 'todos.txt'


def get_todos(filepath = FILEPATH):
    """Opens the mentioned file and returns the todos items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    """Open the mentioned file and writes todos items"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# if we execute the functions file directly the __name__ variable will be set to '__main__' string
# however if we execute the functions module from some other module, __name__ will be set to 'functions'
print(__name__)

# the conditional block below can be used to control which part of code should be executed if the functions module is
# run and which line of code to be executed if the functions module is run from some other module
if __name__ == '__main__':
    print('Functions module is executed directly')