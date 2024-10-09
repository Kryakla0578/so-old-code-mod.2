code = ''

for i in range(3, 21):
    code += str(i) + '-'
    for j in range(1, 21):
        if i <= j:
            break
        for k in range(1, 21):
            if i <= k:
                break
            if i % (j + k) == 0 and j < k:
                code += str(j) + str(k)
    print(code)
    code = ''
