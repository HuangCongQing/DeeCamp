    a = str(oct(i) % 10)
    b = str(oct(i**2) % 10)
    if a[-1] == b[-1]:
        conut = count + 1