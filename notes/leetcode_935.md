[leetcode 935.骑士拨号器](https://leetcode-cn.com/problems/knight-dialer/) 
---
    题目描述大致是按国际象棋里骑士的行走规则在一个数字拨号键盘上从任意起点拨指定位数的数字。
   ![骑士行走规则](https://github.com/goslingl/LeetCode/raw/master/img/knight.png)

   ![数字拨号键盘](https://github.com/goslingl/LeetCode/raw/master/img/keypad.png)

    抽象一下，可以看成是有10个顶点的图，按照指定规则连通，找出指定长度路径有多少条。
   ![抽象连通图](https://github.com/goslingl/LeetCode/raw/master/img/graph.png)

    求长度为N的路径有多少条:
      - 分别计算以每个定点为起点的,长度为N的路径有多少
      - 起点固定，根据连通关系，路径的下一个顶点是确定的集合，问题即可分解为以下一顶点为起点的长度为(N-1)的路径有多少
      - 将递归转换成迭代计算，从路径长度为1迭代到N

   **逻辑实现**
---
    ```scala
    def knightDialer(N: Int): Int = {
        val num = 10
        val mod = 1e9+7
        var graph = Map(0 -> List(4,6), 1 -> List(6,8), 2 -> List(7,9), 3 -> List(4,8), 4 -> List(0,3,9),
                        5 -> List(), 6 -> List(0,1,7), 7 -> List(2,6), 8 -> List(1,3), 9 -> List(2,4))
        var count = Array(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        var sum = 0.0
        for ( i <- 1 until N) {
            var rawCount = count.clone
            for ( j <- 0 until num) {
                var temp = 0.0
                for ( e <- graph(j)) 
                    temp += rawCount(e)
                count(j) = temp%mod
            }
            println((i+1, count.mkString(" ")))
        }
        for ( j <- 0 until num)
            sum += count(j)
        sum %= mod
        return sum.toInt
    }
    ```
