# these below in capital letters is constants variables with constant value
FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return
        the list of to-do.
        """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the txt file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# if __name__ == 'modules.functions':
#     print("welcome to our ToDos")

# print(__name__)
if __name__ == "__main__":
    text = """
    Principles of productivity:
    Managing your inflow.
    systemizing everything that repeat
     """

    print(text)