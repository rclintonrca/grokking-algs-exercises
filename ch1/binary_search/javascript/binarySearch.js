function findMiddle(arr) {
  const middle = Math.floor(arr.length / 2);
  return middle;
}
function search(arr, val, ix = 0) {
  if (arr.length === 0) {
    return null;
  }

  let middleIx = findMiddle(arr);
  let middleVal = arr[middleIx];

  if (val === middleVal) {
    return middleIx + ix;
  } else if (val > middleVal) {
    let arrSlice = arr.slice(middleIx + 1);
    return search(arrSlice, val, middleIx + 1);
  } else if (val < middleVal) {
    let arrSlice = arr.slice(0, middleIx);
    return search(arrSlice, val);
  } else {
    return -1;
  }
}
module.exports = {
  findMiddle,
  search,
};
