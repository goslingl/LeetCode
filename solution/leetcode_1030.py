# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def nextLargerNodes(head):
    s = []
    #if head == None: return []
    #elif head.next == None: return [0]
    ans = []
    #while head:
    #    s.append(head.val)
    #    head = head.next
    s = head
    ss = sorted(s)
    last_val = -1
    last_max = -1
    for idx in range(len(s)-1):
        val = s[idx]
        if val == ss[-1]:
            ans.append(0)
            del(ss[-1])
        if val >= last_val and val < last_max:
            ans.append(last_max)
        else:
            for idx2 in range(idx+1,  len(s)):
                if s[idx2] > val:
                    ans.append(s[idx2])
                    last_max = s[idx2]
                    break
            else:
                ans.append(0)
                #last_max = -1
        last_val = val
    ans.append(0)
    return ans

def main():
    h = [2,1,5]
    print(nextLargerNodes(h))
    h = [2,7,4,3,5]
    print(nextLargerNodes(h))
    h = [1,7,5,1,9,2,5,1]
    print(nextLargerNodes(h))

main()
