# 5016. 删除最外层的括号

def removeOuterParentheses(str):
        out_left = []
        out_right = []
        cnt = 0
        res = ''
        for idx in range(len(str)):
            if str[idx] == '(':
                if cnt == 0:
                    out_left.append(idx)
                else:
                    res += str[idx]
                cnt += 1
            else: # ')'
                if cnt == 1:
                    out_right.append(idx)
                else:
                    res += str[idx]
                cnt -= 1
        return res

def main():
    str = "(()())(())"
    print(removeOuterParentheses(str))
    str = "(()())(())(()(()))"
    print(removeOuterParentheses(str))
    str = "()()"
    print(removeOuterParentheses(str))

main()
