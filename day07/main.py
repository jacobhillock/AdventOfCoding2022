import re
from dataclasses import dataclass

@dataclass
class File:
    size: int
    name: str

@dataclass
class Directory:
    files: list[File]
    sub_dirs: list
    parent: list
    name: str

file_data = ""
with open('input', 'r') as file:
    file_data = file.read()

rows = file_data.split('\n')

fs = Directory([], [], None, '/')
cd = fs

cd_regex = re.compile('^\$ cd (\.\.|\w+|/)')
dir_regex = re.compile('^dir (\w+)')
file_regex = re.compile('^(\d+) ([a-zA-Z.]+)')


def full_path (dir_: Directory):
    if dir_.parent:
        return full_path(dir_.parent)+'/'+dir_.name
    return ''

for row in rows:
    if dir_name:=cd_regex.findall(row):
        name = dir_name[0]
        if name == '..':
            cd = cd.parent
        elif name != '/':
            cd = cd.sub_dirs[[dir.name for dir in cd.sub_dirs].index(dir_name[0])]
    elif (file:=file_regex.findall(row)):
        cd.files.append(File(int(file[0][0]), file[0][1]))
    elif dir_:=dir_regex.findall(row):
        cd.sub_dirs.append(Directory([], [], cd, dir_[0]))

dir_sizes = {}

def flatten(dir_: Directory):
    dir_sizes[full_path(dir_)] = sum([file_.size for file_ in dir_.files])
    for sub in dir_.sub_dirs:
        dir_sizes[full_path(dir_)] += dir_sizes.get(full_path(sub), flatten(sub))
    
    return dir_sizes[full_path(dir_)]

total_used = flatten(fs)
total_size = 70_000_000
needed_space = 30_000_000
to_remove = needed_space - ( total_size - total_used )

print(to_remove)

total = 0
best_dir = ''

for dir_path, size in dir_sizes.items():
    if size <= 100_000:
        total += size
    if size >= to_remove and size < dir_sizes[best_dir]:
        best_dir = dir_path

print('#1', total)
print('#2', dir_sizes[best_dir])