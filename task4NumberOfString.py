str = 'data 48 call 9 read13 blank0a'
abc = len(str)
integ = []
i = 0
while i < abc:
    s_int = ''
    a = str[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < abc:
            a = str[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))

print(integ)