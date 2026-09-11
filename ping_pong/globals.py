

def set_counter(r : int):
    with open('counter.txt', 'w') as counter_file:
        counter_file.write(str(r))

    
def get_counter() -> int:
    with open('counter.txt', 'r') as counter_file:
        return int(counter_file.read())