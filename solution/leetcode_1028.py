def rm_head_0(s):
    if s[0] != '0': return s
    else: return rm_head_0(s[1:])

def baseNeg2(N):
        if N == 0: return '0'
        b = '00' + bin(N)[2:]
        b_len = len(b)
        ans = [ int(b[b_len-1-idx]) for idx in range(b_len) ]
        #print(ans)
        for idx in range(1, b_len-2, 2):
            if ans[idx] > 0:
                ans[idx+1] += 1
        #print(ans)
        for idx in range(0, b_len-2, 2):
            if ans[idx] == 2:
                ans[idx] = 0
                if ans[idx+1] == 1: # 1,0/1
                    ans[idx+1] = 0
                elif ans[idx+2] == 0: # 0,0
                    ans[idx+1], ans[idx+2] = 1, 1
                else: # 0,1
                    ans[idx+1], ans[idx+2] = 1, 2
        #print(ans)
        return rm_head_0(''.join([str(idx) for idx in ans[::-1]]))

def main():
    for idx in range(33):
        print(idx, baseNeg2(idx), '\n')

main()

