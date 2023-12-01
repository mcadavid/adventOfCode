import sys
class Dir:
    def __init__(self, name, dirs, parentDir = None, size = 0):
        self.name = name
        self.parentDir = parentDir
        self.dirs = dirs
        self.size = size
        self.files = []


f = open("input.txt")


commands = []
for line in f:
    line = line[:-1]
    commands.append(line)

for i in range(50):
    commands.append('$ cd ..')

count = 0
print(len(commands))
while count < len(commands):
    line = commands[count]
    print(line)
    if line == '$ cd /':
        currentDir = Dir("root", dict())
        root = currentDir
    elif line == '$ ls':
        count += 1
        continue
    elif line.startswith("dir"):
        _, name = line.split()
        currentDir.dirs[name] = Dir(name, dict(), currentDir)
    elif line == '$ cd ..':
        if currentDir == root:
            break
        currentDirSize = currentDir.size
        currentDir = currentDir.parentDir
        currentDir.size += currentDirSize
    elif line.startswith("$ cd "):
        _, _, name = line.split()
        currentDir = currentDir.dirs[name]
    else:
        size, name = line.split()
        currentDir.size += int(size)
        currentDir.files.append(name)
    count += 1

# currentDir.parentDir.size += currentDir.size

print('\n')

def navigate(currentDir):
    global total
    global space
    if len(currentDir.dirs) == 0:
        return

    for dir in currentDir.dirs.values():
        space += 1
        star = ''
        if dir.size < 100000:
            total += dir.size
            star = '*'
        print(' ' * space + '-', dir.name, dir.files, dir.size, star)
        navigate(dir)
        space -= 1

space = 0
total = 0
navigate(root)
print("total =", total)

print("====================")
print("second task")
print("====================")

total_used_space = 0
print("total used space", root.size)
space_to_be_freed = root.size - 40000000
print("space to be freed", space_to_be_freed)


def find_size(cDir):
    global size
    if len(cDir.dirs) == 0:
        return
    if cDir.size >= space_to_be_freed:
        size = min(cDir.size, size)

    for dir in cDir.dirs.values():
        if dir.size >= space_to_be_freed:
            size = min(dir.size, size)
            print(dir.name)
        find_size(dir)


size = sys.maxsize
find_size(root)
print("Size smallest  dir to delete", size)
