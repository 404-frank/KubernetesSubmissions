

def set_random_string(r : str):
    with open('files/vars.txt', 'w') as vars_file:
        vars_file.write(r)

    
def get_random_string() -> str:
    with open('files/vars.txt', 'r') as vars_file:
        return vars_file.read()