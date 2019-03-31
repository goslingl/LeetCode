
#def prefixesDivBy5(A: List[int]) -> List[bool]:
def prefixesDivBy5(A):
        sum = 0
        ans = []
        for idx in range(len(A)):
            sum = sum * 2 + A[idx]
            if sum % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans

def main():
    A = [0,1,1]
    print(prefixesDivBy5(A))
    A = [1,1,1]
    print(prefixesDivBy5(A))
    A = [0,1,1,1,1,1]
    print(prefixesDivBy5(A))
    A = [1,1,1,0,1]
    print(prefixesDivBy5(A))

main()

