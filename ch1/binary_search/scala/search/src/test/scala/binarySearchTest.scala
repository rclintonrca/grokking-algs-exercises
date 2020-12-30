import org.scalatest.flatspec.AnyFlatSpec

class binarySearchTest extends AnyFlatSpec {

  val arrEven = Array(1,2,3,4)
  val arrOdd = Array(1,2,3,4,5)

  it should "find the middle of an odd array " in {
    assert(binarySearch.findMiddle(arrOdd) === 2)
  }
  it should "find the middle of an EVEN array " in {
    assert(binarySearch.findMiddle(arrEven) === 2)
  }



  it should "find a number when its the middle index of an arr" in {
    assert(binarySearch.search(arrOdd, 3) === 2)
  }
  it should "find a number when its the upper index of an arr" in {
    assert(binarySearch.search(arrOdd, 4) === 3)
  }
  it should "find a number when its the lower index of an arr" in {
    assert(binarySearch.search(arrOdd, 2) === 1)
  }
  it should "return -1 when a number is not in the arr" in {
    assert(binarySearch.search(arrOdd, -999) === -1)
  }
  it should "empty arr returns -1 (bad practice to return null in functs" in {
    assert(binarySearch.search(Array(), -999) === -1)
  }
}
