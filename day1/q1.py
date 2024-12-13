with open("input.txt", "r") as f:
    line = f.read().replace("\n", "")
    curr = 0
    for l in line:
        if l == "(":
            curr += 1
        else:
            curr -= 1
    print(curr)
