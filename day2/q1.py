with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.replace("\n", "")
        [l, w, h] = [int(l) for l in line.split("x")]
        surfaceAreaSub2 = [l * w, w * h, h * l]
        slack = min(surfaceAreaSub2)
        total += sum([2 * sa for sa in surfaceAreaSub2]) + slack
    print(total)
