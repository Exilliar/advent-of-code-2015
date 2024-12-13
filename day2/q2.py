with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.replace("\n", "")
        [l, w, h] = [int(l) for l in line.split("x")]
        cubicFeet = l * w * h
        wrapAround = 0
        if l == w and w == h:
            wrapAround = 4 * l
        else:
            largest = max([l, w, h])
            if l == largest:
                wrapAround += (2 * w) + (2 * h)
            elif w == largest:
                wrapAround += (2 * l) + (2 * h)
            elif h == largest:
                wrapAround += (2 * w) + (2 * l)
        total += wrapAround + cubicFeet
    print(total)
