import os

for i in range(1, 26):
    if not os.path.exists(f"{i}.1.py"):
        with open(f"{i}.1.py", "w") as fd:
            fd.write(f'with open("{i}.txt", "r") as f:\n    data = f.read().strip()')

    if not os.path.exists(f"{i}.2.py"):
        with open(f"{i}.2.py", "w") as fd:
            pass

    if not os.path.exists(f"{i}.txt"):
        with open(f"{i}.txt", "w"):
            pass
