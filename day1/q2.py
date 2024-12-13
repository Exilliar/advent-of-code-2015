with open("input.txt", "r") as f:
    line = f.read().replace("\n", "")
    curr = 0
    pos = 1
    for l in line:
        if l == "(":
            curr += 1
        else:
            curr -= 1
        if curr == -1:
            break
        else:
            pos += 1
    print(pos)
