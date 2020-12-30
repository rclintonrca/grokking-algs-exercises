import org.scalatest.flatspec.AnyFlatSpec

class CubeCalculatorTest extends AnyFlatSpec {
  it should "calc 3 cubed correctly" in {
    assert(CubeCalculator.cube(3) === 27)
  }
}
