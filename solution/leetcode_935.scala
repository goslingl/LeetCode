object Solution {
    def main(args: Array[String]) {
        //for ( i <- 1 until 10) {
        //    val v = knightDialer(i)
        //    println((i, v))
        //    println((161, knightDialer(161)))
        //}
        println((161, knightDialer(161)))
    }
 
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
}
