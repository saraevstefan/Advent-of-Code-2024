with open('5.txt', 'r') as f:
    data = f.read()


sections = data.split('\n\n')

dct_section, lst_orders = data.split('\n\n')

def create_dct_predecessors(dct_section):
    dct_predecessors = {}
    for line in dct_section.split('\n'):
        key, value = line.split('|')
        key = int(key)
        value = int(value)
        if key not in dct_predecessors:
            dct_predecessors[key] = []
        dct_predecessors[key].append(value)
    return dct_predecessors

dct_predecessors = create_dct_predecessors(dct_section)

def check_before(num, list_before_num):
    for i, el in enumerate(list_before_num):
        if el in dct_predecessors and num not in dct_predecessors[el]:
            return False, i
        if num in dct_predecessors and el in dct_predecessors[num]:
            return False, i
    return True, 0

def check_after(num, list_after_num):
    for i, el in enumerate(list_after_num):
        if num in dct_predecessors and el not in dct_predecessors[num]:
            return False, i
        if el in dct_predecessors and num in dct_predecessors[el]:
            return False, i
    return True, 0

def check_good(order):
    # returns middle value
    for i in range(len(order)):
        number = order[i]
        lst_before = order[:i]
        lst_after = order[i+1:]
        before_good, _ = check_before(number, lst_before)
        after_good, _ = check_after(number, lst_after)
        if not before_good or not after_good:
            return 0
    return order[len(order) // 2]

def check_bad(order):
    # returns middle value
    is_bad = True
    is_truly_bad = False
    while is_bad:
        is_bad = False
        before_index = 0
        after_index = 0
        for i in range(len(order)):
            number = order[i]
            lst_before = order[:i]
            lst_after = order[i+1:]
            before_good, before_index = check_before(number, lst_before)
            after_good, after_index = check_after(number, lst_after)
            if not before_good or not after_good:
                is_bad = True
                if not is_truly_bad:
                    is_truly_bad = True
                    # print("found bad order: ", order)
                break
        
        # swap indexes
        if not before_good:
            # print("swapping before: ", order[i], order[before_index])
            order[i], order[before_index] = order[before_index], order[i]
        if not after_good:
            # print("swapping after: ", order[i], order[i + after_index + 1])
            order[i], order[i + after_index + 1] = order[i + after_index + 1], order[i]
    if not is_truly_bad:
        return 0
    return order[len(order) // 2]

S = 0
for order in lst_orders.split('\n'):
    lst_numbers = list(map(int, order.split(',')))
    S += check_bad(lst_numbers)
    
print(S)