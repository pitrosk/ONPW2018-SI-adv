def min_max_arg(l):
    mi, ma = l[0], l[0]
    imi, ima = 0, 0
    for i in range(len(l)):
        if l[i] < mi:
            mi = l[i]
            imi = i
        if l[i] > ma:
            ma = l[i]
            ima = i
    return imi, ima
    