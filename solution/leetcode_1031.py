import queue

def numEnclaves(A):
    '''
    1.按边界做广度优先搜索，做标记
    2.遍历比较标记，得到结果
    '''
    line = len(A)
    col = len(A[0])
    mark = [ [0 for idx in range(col) ] for idx2 in range(line) ]
    move = [ [1,0], [-1,0], [0,1], [0, -1]]
    q = queue.Queue()

    # get bound land
    for idx in range(line):
        for idx2 in range(col):
            if (idx == 0 or idx == line-1 or idx2 == 0 or idx2 == col-1) and A[idx][idx2]:
                q.put(idx * col + idx2)
                mark[idx][idx2] = 1

    while q.empty() == False:
        val = q.get()
        x, y = val//col, val%col
        for idx in range(len(move)):
            new_x = x + move[idx][0]
            new_y = y + move[idx][1]
            if new_x >=0 and new_x < line and new_y >= 0 and new_y < col:
                if A[new_x][new_y] == 1 and mark[new_x][new_y] == 0:
                    q.put(new_x * col + new_y)
                    mark[new_x][new_y] = 1

    ans = 0
    for idx in range(line):
        for idx2 in range(col):
            if A[idx][idx2] == 1 and mark[idx][idx2] == 0:
                ans += 1

    return ans

A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(numEnclaves(A))
A = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(numEnclaves(A))

