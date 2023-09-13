/*

make a staircase shape

*/

object App {
  def main(args: Array[String]): Unit = {
    var n = 10
    var i = 1
    val space = " "
    val char = "#"

    while(n > 0) {
      println(s"${space * (n-1)}${char * i}")
      n -= 1
      i += 1
    }
  }
}