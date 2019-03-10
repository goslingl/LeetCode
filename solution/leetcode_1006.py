def clumsy(N):
    e = ''
    op = [ '*', '//', '+', '-']
    for idx in range(N):
        e = e + str(N-idx)
        if N-idx > 1:
            e = e + op[idx%4]
    print(e)
    return eval(e)

print(clumsy(4))
print(clumsy(10))
