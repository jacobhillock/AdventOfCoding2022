from dataclasses import dataclass

file_data = ""
with open('input', 'r') as file:
    file_data = file.read()

forest = []
width = -1
height = -1


def multiply_all(numbers: list[int]) -> int:
    value = 1
    for number in numbers:
        value *= number
    return value


def determine_visible(x: int, y: int) -> bool:
    west, east, north, south = True, True, True, True
    scores = [0, 0, 0, 0]
    tree = forest[x][y]

    for i in reversed(range(0, x)):
        scores[0] += 1
        if forest[i][y].size >= tree.size:
            west = False
            break

    for i in range(x + 1, width):
        scores[1] += 1
        if forest[i][y].size >= tree.size:
            east = False
            break

    for j in reversed(range(0, y)):
        scores[2] += 1
        if forest[x][j].size >= tree.size:
            north = False
            break

    for j in range(y + 1, height):
        scores[3] += 1
        if forest[x][j].size >= tree.size:
            south = False
            break

    return any([north, south, east, west]), multiply_all(scores)


@dataclass
class Tree:
    size: int
    visible: bool
    score: int


rows = file_data.split('\n')

# build the forest
for i, row in enumerate(rows):
    forest.append(list())
    for j, tree in enumerate(row):
        new_tree = Tree(int(tree), True, 0)
        forest[i].append(new_tree)

width = len(forest[0])
height = len(forest)

for i, row in enumerate(rows[1:-1]):
    for j, tree in enumerate(row[1:-1]):
        forest[i+1][j+1].visible, forest[i+1][j +
                                              1].score = determine_visible(i+1, j+1)

visibles = []
scores = []
for row in forest:
    visibles.extend([tree.visible for tree in row])
    scores.extend([tree.score for tree in row])

print('#1',  sum(visibles))
print('#2',  max(scores))
