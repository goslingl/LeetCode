import time

# 将特殊质数2事先放在列表中
t = [2]
count = 1
# 去掉所有偶数，从3开始迭代，步进为2
for x in range(3, 100000, 2):
    # 所有大于10的质数中，个位数只有1、3、7、9，大于5且以5结尾的整数能被5整除，这里首先过滤掉大于5且以5结尾的整数
    if x > 5 and x % 10 == 5:
        continue
    # 除去2之外，质数的因子中肯定是没有2的，这里去掉所有被除数中的偶数
    # 一个整数的前后对应的两个因子的乘积等于这个整数，所以一个整数如果平方根之前有一个因子，那平方根之后肯定有一个对应的因子，中间是平方根
    # 这里使用平方根极大减小了数据规模，以及减少了大量迭代次数
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            break
    # 要格外注意一下这里的else语句的执行逻辑
    # 没有进入for循环、以及for循环正常结束都会执行else语句，如果被break中断，else不会执行
    else:
        count += 1
        t.append(x)

print(t)