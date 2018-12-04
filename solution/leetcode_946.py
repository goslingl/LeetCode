# pass

class Solution:
    def validateStackSequences(self, pushed, popped):
        res = False
        if len(pushed) != len(popped):  return res
        temp = []
        pop_idx, push_idx, temp_idx = 0, 0, -1
        pop_len = len(popped)
        while pop_idx < pop_len:
            #if temp_idx == pop_len-1 and temp[temp_idx] != popped[pop_idx]:
            #    break
            if push_idx < pop_len and popped[pop_idx] == pushed[push_idx]:
                pop_idx += 1
                push_idx += 1
            elif temp_idx >= 0 and popped[pop_idx] == temp[temp_idx]:
                pop_idx += 1
                temp = temp[:temp_idx]
                temp_idx -= 1
            elif push_idx < pop_len:
                temp.append(pushed[push_idx])
                temp_idx += 1
                push_idx += 1
            else:
                break
        if pop_idx == pop_len: res = True
        #print('pop_idx, push_idx, temp_idx:', pop_idx, push_idx, temp_idx)
        return res

if __name__ == '__main__':
        s = Solution()
        pushed = [1,2,3,4,5]
        popped = [4,5,3,2,1]
        res = s.validateStackSequences(pushed, popped)
        print(pushed, popped, res)
        pushed = [1,2,3,4,5]
        popped = [4,3,5,1,2]
        res = s.validateStackSequences(pushed, popped)
        print(pushed, popped, res)
