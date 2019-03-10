
#def largestSumAfterKNegations(A: List[int], K: int) -> int:
def largestSumAfterKNegations(A, K) -> int:
    sortedA = sorted(A)
    neg = 0
    for idx in range(len(A)):
        if sortedA[idx] >= 0:
            neg = idx
            break
    result = 0
    if K <= neg:
        result = sum(sortedA[K:]) - sum(sortedA[:K])
    else:
        min_ = min(abs(sortedA[neg-1]), sortedA[neg])
        flag = ((K - neg) % 2) * 2
        print('min_=%d, flag=%d' % (min_, flag))
        result = sum(sortedA[neg:]) - sum(sortedA[:neg]) - min_ * flag
    return result

def main():
    A = [4,2,3]; K = 1
    print(largestSumAfterKNegations(A, K))
    A = [3,-1,0,2]; K = 3
    print(largestSumAfterKNegations(A, K))
    A = [2,-3,-1,5,-4]; K = 2
    print(largestSumAfterKNegations(A, K))

main()
