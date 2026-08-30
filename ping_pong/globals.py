

def set_counter(r : int):
    with open('shared-files/counter.txt', 'w') as counter_file:
        counter_file.write(r)

    
def get_counter() -> int:
    with open('shared-files/counter.txt', 'r') as counter_file:
        return int(counter_file.read())