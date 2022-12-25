rows = []

def split_pair(row: str) -> list[list[int]]:
    pairs = row.split(',')
    ranges = []
    for pair in pairs:
        ranges.append([int(value) for value in pair.split('-')])
    return ranges

def fully_contains(row: list[list[int]]) -> bool:
    return (row[0][0] >= row[1][0] and row[0][1] <= row[1][1]) or (row[0][0] <= row[1][0] and row[0][1] >= row[1][1])

def partially_contain(row: list[list[int]]) -> bool:
    # [[7, 94], [96, 99]] false
    # [[46, 63], [38, 62]] true
    return len([
        value for value in row[0] if row[1][0] <= value  and  value <= row[1][1]
    ]) > 0 or len([
        value for value in row[1] if row[0][0] <= value  and  value <= row[0][1]
    ]) > 0

with open('day4.input', 'r') as file:
    rows = list(filter(lambda value: value != '',file.read().split('\n')))


ranges = list(map(split_pair, rows))
rows_fully_contain = list(map(fully_contains, ranges))
print('#1', sum(rows_fully_contain))

rows_partially_contain = list(map(partially_contain, ranges))
print('#2', sum(rows_partially_contain))