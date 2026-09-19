

def set_stamp(r : str):
    with open('stamp.txt', 'w') as stamp_file:
        stamp_file.write(r)

    
def get_stamp() -> str:
    with open('stamp.txt', 'r') as stamp_file:
        return stamp_file.read()
    
def get_file_content(file_name: str) -> str:
    with open(file_name, 'r') as file_handle:
        return file_handle.read()
        