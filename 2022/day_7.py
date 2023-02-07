import itertools


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.sub_files = {}
        self.sub_dirs = {}
        self.size = None

    def get_size(self):
        if self.size is not None:
            return self.size
        self.size = 0
        if len(self.sub_files) > 0:
            self.size += sum([sub_file.size for sub_file in self.sub_files.values()])
        if len(self.sub_dirs) > 0:
            self.size += sum([sub_dir.get_size() for sub_dir in self.sub_dirs.values()])
        return self.size

    def add_dir(self, dir_name):
        if dir_name not in self.sub_dirs.keys():
            self.sub_dirs[dir_name] = Dir(name=dir_name, parent=self)

    def add_file(self, file_name, file_size):
        if file_name not in self.sub_files.keys():
            self.sub_files[file_name] = File(name=file_name, size=file_size)

    def tree(self, depth=0):
        print("  " * depth + "- " + str(self.name) + " (dir)")
        depth += 1
        for sub_dir in self.sub_dirs.values():
            sub_dir.tree(depth)
        for file in self.sub_files.values():
            print("  " * depth + "- " + file.name + " (file, size=" + str(file.size) + ")")


class FileSystem:

    def __init__(self):
        self.current_dir = None
        self.root_dir = Dir(name="/", parent=None)

    def cd(self, arg):
        if arg == "/":
            self.current_dir = self.root_dir
        elif arg == "..":
            self.current_dir = self.current_dir.parent
        else:
            self.current_dir = self.current_dir.sub_dirs.get(arg)

    def ls(self, arg: str):
        args: list = arg.split()
        if args[0] == "dir":
            self.current_dir.add_dir(dir_name=args[1])
        else:
            self.current_dir.add_file(file_name=args[1], file_size=int(args[0]))

    def load_data(self, data_path):
        for line in open(data_path):
            cmd = line.split()
            if cmd[0] == "$":
                if cmd[1] == "cd":
                    self.cd(cmd[2])
            else:
                self.ls(line)


def day_7_task_1_rec(dir):
    if dir.get_size() <= 100000:
        if len(dir.sub_dirs) > 0:
            return dir.get_size() + sum([day_7_task_1_rec(sub_dir) for sub_dir in dir.sub_dirs.values()])
        return dir.get_size()
    return sum([day_7_task_1_rec(sub_dir) for sub_dir in dir.sub_dirs.values()])


def day_7_task_1_example():
    files = FileSystem()
    files.load_data(data_path="data/day7_test.txt")
    files.root_dir.tree()
    result = day_7_task_1_rec(files.root_dir)
    assert result == 95437
    return result


def day_7_task_1():
    files = FileSystem()
    files.load_data(data_path="data/day7.txt")
    # files.root_dir.tree()
    result = day_7_task_1_rec(files.root_dir)
    assert result == 1206825
    return result


def day_7_task_2_get_candidate(dir, disk_space_needed):
    candidates = list(itertools.chain.from_iterable(
        [day_7_task_2_get_candidate(sub_dir, disk_space_needed) for sub_dir in dir.sub_dirs.values()]))
    if dir.get_size() >= disk_space_needed:
        return [(dir.name, dir.get_size())] + candidates
    return candidates


def day_7_task_2_example():
    total_disk_space = 70000000
    unused_space_needed = 30000000
    total_size_occupied = 48381165
    disk_space_needed = abs(total_disk_space - total_size_occupied - unused_space_needed)
    files = FileSystem()
    files.load_data(data_path="data/day7_test.txt")
    assert total_size_occupied == files.root_dir.get_size()
    candidates = day_7_task_2_get_candidate(files.root_dir, disk_space_needed)
    solution = min([x[1] for x in candidates])
    assert solution == 24933642
    return solution


def day_7_task_2():
    total_disk_space = 70000000
    unused_space_needed = 30000000
    files = FileSystem()
    files.load_data(data_path="data/day7.txt")
    total_size_occupied = files.root_dir.get_size()
    disk_space_needed = abs(total_disk_space - total_size_occupied - unused_space_needed)
    candidates = day_7_task_2_get_candidate(files.root_dir, disk_space_needed)
    solution = min([x[1] for x in candidates])
    assert solution == 9608311
    return solution


if __name__ == '__main__':
    print("Example:")
    day_7_task_1_example()
    print("\nAnswer 1:", day_7_task_1())
    day_7_task_2_example()
    print("Answer 2:", day_7_task_2())
