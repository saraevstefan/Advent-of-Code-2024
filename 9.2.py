def search_for_free_space(disk, length, end_index):
    for entry in disk:
        entry_is_free, entry_id_nr, entry_length, entry_start_index = entry
        if entry_is_free == False:
            # discard occupied space
            continue
        if entry_length < length:
            # discard too short space
            continue
        if entry_start_index >= end_index:
            # discard space that is too far
            return None
        return entry
    return None

def merge_free_spaces(disk, neighbor_index):
    i = max(0, neighbor_index - 3)
    touched_positions = 0
    while i < len(disk) - 1 and touched_positions < 7:
        if disk[i][0] == True and disk[i+1][0] == True:
            disk[i] = (True, 0, disk[i][2] + disk[i+1][2], disk[i][3])
            disk.pop(i+1)
        else:
            i += 1
        touched_positions += 1
    return

def print_disk(disk):
    for entry in disk:
        is_free, id_nr, length, start_index = entry
        if is_free == True:
            print("." * length, end="")
        else:
            print(str(id_nr) * length, end="")
    print()

def create_disk(disk):
    summary_disk = disk
    L = sum([x[2] for x in summary_disk])
    
    disk = [0] * L
    
    for entry in summary_disk:
        is_free, id_nr, length, start_index = entry
        if is_free == True:
            for i in range(length):
                disk[start_index + i] = 0
        else:
            for i in range(length):
                disk[start_index + i] = id_nr + 1
    
    return disk

with open("9.txt", "r") as f:
    data = f.read().strip()

data = [int(x) for x in data]

disk = []  # (is_free, id_nr, length, start_index)

index = 0
for i, x in enumerate(data):
    if x == 0:
        continue
    if i % 2 == 0:
        id_nr = i // 2 
        disk.append((False, id_nr, x, index))
        index += x
    else:
        disk.append((True, 0, x, index))
        index += x

disk_copy = disk.copy()

for entry in disk_copy[::-1]:
    is_free, id_nr, length, start_index = entry
    
    if id_nr == 3:
        a = 1
    
    if is_free == True:
        continue

    # print_disk(disk)
    # entry[0] == False

    # find first free space until start_index
    free_space = search_for_free_space(disk, length, start_index)
    if free_space == None:
        continue

    # free_space[0] == True

    # first, pop the current entry and create free space there
    entry_index = disk.index(entry)
    disk.pop(entry_index)
    disk.insert(entry_index, (True, 0, length, start_index))

    # add current entry to free space
    free_space_index = disk.index(free_space)
    disk.pop(free_space_index)
    disk.insert(free_space_index, (False, id_nr, length, free_space[3]))
    
    if free_space[2] > length:
        disk.insert(free_space_index+1, (True, 0, free_space[2] - length, free_space[3] + length))

    # next, merge existing free space with new free space
    merge_free_spaces(disk, entry_index)
    # not necessary, we preserve an ivariant that there are no two free spaces next to each other
    # we can only break this invariant when we pop an occupied entry and insert a free space there
    # and we fix this with the call above. There is only a special case, where we move an entry to its left neighbor
    # and we basically need to merge the empty space of the entry with the remaining empty space from the left neighbor,
    # but we do it by looking in a window of 7 positions (entry_index - 3 to entry_index + 3) and merging all free spaces
    # that we encounter
    # merge_free_spaces(disk, free_space_index)

# print_disk(disk)

disk = create_disk(disk)

S = 0

for i in range(len(disk)):
    if disk[i] == 0:
        continue

    S += (disk[i] - 1) * i

print(S)