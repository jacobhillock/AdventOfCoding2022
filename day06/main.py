file_data = ""
with open('day6.input', 'r') as file:
    file_data = file.read()

def find_start(string: str, pack_size: int) -> int:
    for i in range(len(string)-pack_size):
        check = list(set(string[i:i+pack_size]))
        if len(check) == pack_size:
            return i + pack_size

print('#1', find_start(file_data, 4))
print('#2', find_start(file_data, 14))
