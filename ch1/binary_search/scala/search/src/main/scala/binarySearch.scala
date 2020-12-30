
object binarySearch extends App {
  def findMiddle(arr: Array[Int]): Int = {
    Math.round(Math.floor(arr.length / 2)).toInt
  }

  def search(arr: Array[Int], value: Int, ix: Int = 0): Int = {

    if (arr.length  == 0 ) {
      return -1
    }

    val middleIx = findMiddle(arr)
    val middleVal = arr(middleIx)

    if (value == middleVal) {
      middleIx + ix
    } else if (value > middleVal) {
      val arrSlice = arr.slice(middleIx + 1,arr.length + 1)
      search(arr=arrSlice, value=value, ix=middleIx +1)
    } else if (value < middleVal) {
      val arrSlice = arr.slice(0,middleIx)
      search(arr=arrSlice, value=value, ix=ix)
    } else {
      -1
    }
  }

  val dummyArr = Array(1, 2, 3)

  println(findMiddle(dummyArr))

}
