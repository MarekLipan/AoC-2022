import re

# read the input into a list
file = open('Day-7/input.txt', 'r')
L = file.read().splitlines()

def size_of_dirs(l: list, max_size: int) -> int:
    """
    Find directories with at most max size in the tree and output their total siza
    """

    in_dirs = ["/"]
    all_dirs = {"/": 0}

    for i in l:
        if i == "$ cd /":
            continue
        elif i == "$ ls":
            continue
        elif i == "$ cd ..":
            in_dirs.pop()
        elif i[:4] == "$ cd":
            dir_path = in_dirs[-1] + "/" + i[5:] 
            in_dirs.append(dir_path)
        elif i[:3]=="dir":
            # add the whole path as dir name for uniqueness
            dir_path = in_dirs[-1] + "/" + i[4:]
            if dir_path not in all_dirs:
                all_dirs[dir_path] = 0
        else:
            filesize = int(re.findall(r'\d+', i)[0])
            for d in in_dirs:
                all_dirs[d] += filesize
        
    result = 0
    for v in all_dirs.values():
        if v <= max_size:
            result += v

    print(result)

    return all_dirs

all_dirs = size_of_dirs(L, 100000)


def dir_to_delete_size(all_dirs: dict, F: int, S: int) -> int:
    """
    Find the size of the smallest directory to be deleted so that there is atleast S of the unused space in the filesystem of system of size F
    """

    result = F

    total_used_space = all_dirs["/"]
    
    for d in all_dirs:
        if (total_used_space - all_dirs[d] + S <= F) and (all_dirs[d] < result):
            result = all_dirs[d]

    return result


print(dir_to_delete_size(all_dirs, 70000000, 30000000))





    
    

