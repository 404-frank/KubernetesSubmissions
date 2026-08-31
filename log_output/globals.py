

def set_stamp(r : str):
    with open('sharedfiles/stamp.txt', 'w') as stamp_file:
        stamp_file.write(r)

    
def get_stamp() -> str:
    with open('sharedfiles/stamp.txt', 'r') as stamp_file:
        return stamp_file.read()
    
def get_counter() -> int:
    with open('sharedfiles/counter.txt', 'r') as counter_file:
        return counter_file.read()