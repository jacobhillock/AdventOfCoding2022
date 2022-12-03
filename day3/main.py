import string

priority_list = string.ascii_lowercase + string.ascii_uppercase

def split_sack(sack: str, compartment_count: int =2) -> list[str]:
    size = len(sack)
    compartment_size = size // compartment_count
    compartments = []
    for i in range(compartment_count):
        compartments.append(sack[i*compartment_size:(i+1)*compartment_size])
    return compartments

def find_match(compartments: list[str]) -> str:
    for letter in compartments[0]:
        if letter in compartments[1]:
            return letter

def get_priority (letter: str) -> int:
    return priority_list.index(letter) + 1

def get_sack_groups (sacks:list[str], group_size: int=3) -> list[str]:
    groups = []
    print(list(range (0, len(sacks), group_size)))
    for i in range (0, len(sacks), group_size):
        for letter in sacks[i]:
            shared_sacks = [sack for sack in sacks[i:i + group_size] if letter in sack]
            if len(shared_sacks) == group_size:
                groups.append(letter)
                break
    return groups

sacks = []

with open('day3.input', 'r') as file:
    sacks = file.read().split('\n')
sack_compartments = list(map(split_sack, sacks))
shared_items = list(map(find_match, sack_compartments))
priorities = list(map(get_priority, shared_items))

print('#1', sum(priorities))

groups = get_sack_groups(sacks)
print(groups[1])
priorities = list(map(get_priority, groups))

print('#2', sum(priorities))