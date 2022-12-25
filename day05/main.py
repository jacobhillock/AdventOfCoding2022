import re
from dataclasses import dataclass

@dataclass
class Moves:
    count: int
    start: str
    end: str

class Board:
    def __init__(self, board: list[str], column: list[str]):
        self.board = {}
        
        for i, c in enumerate(column):
            j = len(board) - (len(column) - i)
            while j > 0:
                spot = board[j]
                if spot != ' ':
                    self.board[c] = self.board.get(c, []) + [spot]

                j -= len(column)

    def move(self, how: Moves):
        for _ in range(how.count):
            if len(self.board[how.start]) > 0:
                self.board[how.end].append(self.board[how.start][-1])
                self.board[how.start] = self.board[how.start][:-1]
    
    def move_group(self, how: Moves):
        # for _ in range(how.count):
        #     if len(self.board[how.start]) > 0:
        start = -1*how.count if (-1*how.count + len(self.board[how.start])) > 0 else 0
        self.board[how.end] = self.board[how.end] + self.board[how.start][start:]
        self.board[how.start] = self.board[how.start][:start]
    
    def get_tops(self):
        tops = []
        for key, value in self.board.items():
            tops.append(value[-1] if len(value) > 0 else ' ')
        
        return ''.join(tops)

    def __str__(self):
        return str(self.board)

file_data = ""
with open('day5.input', 'r') as file:
    file_data = file.read()

file_split = file_data.split('\n\n')

move_regex = re.compile('^move (\d+) from (\d+) to (\d+)$', re.MULTILINE)
moves = list(map(lambda x: Moves(int(x[0]), x[1], x[2]), move_regex.findall(file_split[1])))

board_regex = re.compile('.(\D).?\s?', re.MULTILINE)
column_regex = re.compile('.(\d).?\s?', re.MULTILINE)

board_matches = board_regex.findall(file_split[0])
column_matches = column_regex.findall(file_split[0])
board_matches = board_matches[:-1*len(column_matches)]

board1 = Board(board_matches, column_matches)
board2 = Board(board_matches, column_matches)

for move in moves:
    board1.move(move)
    board2.move_group(move)

print('#1', board1.get_tops())
print('#2', board2.get_tops())

# print(board2)
# board2.move_group(moves[0])
# print(moves[0])
# print(board2)