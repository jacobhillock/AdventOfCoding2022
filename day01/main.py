data = ''
with open('day1.input', 'r') as file:
    data = file.read()

elves_str = data.split('\n\n')

elves = []
for elf_str in elves_str:
    cals = [int(cal) for cal in elf_str.split('\n') if cal != '']
    elves.append((sum(cals), cals))

elves = list(sorted(elves, reverse=True, key=lambda x: x[0]))

# ans 1
print(sum([elf[0] for elf in elves[:1]]))

# ans 2
print(sum([elf[0] for elf in elves[:3]]))

