const binarySearch = require('./binarySearch');
const testArrEven = [1, 2, 3, 4];
const testArrOdd = [1, 2, 3, 4, 5];

// TEST Find Middle

test('Returns the 3rd of 5 index for the middle in our Odd arr', () => {
  // console.log("Arr: " + testArrOdd)
  const middleIx = binarySearch.findMiddle(testArrOdd);
  // console.log("middle: " + middleIx)
  expect(middleIx).toBe(2);
});

test('Returns 2nd of 4 for the middle in our Even arr', () => {
  // console.log("Arr: " + testArrEven)
  const middleIx = binarySearch.findMiddle(testArrEven);
  // console.log("middleIx: " + middleIx)
  expect(middleIx).toBe(2);
});

// TEST Search

test('Finds a value when at the middle index', () => {
  const ix = binarySearch.search(testArrOdd, 3);
  console.log('arr: ' + testArrOdd);
  console.log('ix: ' + ix);
  expect(ix).toBe(2);
});

test('Finds a value when at the top', () => {
  const ix = binarySearch.search(testArrOdd, 1);
  console.log('arr: ' + testArrOdd);
  console.log('ix: ' + ix);
  expect(ix).toBe(0);
});

test('Finds a value when at the bottom', () => {
  const ix = binarySearch.search(testArrOdd, 5);
  console.log('arr: ' + testArrOdd);
  console.log('ix: ' + ix);
  expect(ix).toBe(4);
});

test('Returns null when value when the value does not exist in the arr', () => {
  const ix = binarySearch.search(testArrOdd, -1);
  console.log('arr: ' + testArrOdd);
  console.log('ix: ' + ix);

  expect(ix).toBe(null);
});

test('Returns null when arr is empty', () => {
  const ix = binarySearch.search([], -1);
  expect(ix).toBe(null);
});
