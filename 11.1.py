import functools


with open("11.txt", "r") as f:
    data = f.read().strip()

numbers = [int(x) for x in data.split(" ")]


def get_digits(nr):
    digits = []
    while nr > 0:
        digits.append(nr % 10)
        nr = nr // 10
    return digits[::-1]


@functools.lru_cache(maxsize=None)
def get_nr_multiplications_after_split(nr, nr_splits):
    if nr_splits == 0:
        return 1

    if nr == 0:
        return get_nr_multiplications_after_split(1, nr_splits - 1)

    digits = get_digits(nr)
    if len(digits) % 2 == 0:
        left_nr = 0
        for d in digits[: len(digits) // 2]:
            left_nr *= 10
            left_nr += d

        right_nr = 0
        for d in digits[len(digits) // 2 :]:
            right_nr *= 10
            right_nr += d

        return get_nr_multiplications_after_split(
            left_nr, nr_splits - 1
        ) + get_nr_multiplications_after_split(right_nr, nr_splits - 1)

    return get_nr_multiplications_after_split(nr * 2024, nr_splits - 1)


S = sum((get_nr_multiplications_after_split(x, 25)) for x in numbers)

print(S)
