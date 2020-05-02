function isContinuityNum(num) {
  var i = num[0];
  var isContinuation = true;
  for (let e in num) {
    if (num[e] !== i) {
      isContinuation = false;
      break
    }
    i ++;
  }
  console.log(isContinuation);
  return isContinuation
}

isContinuityNum([1, 2, 3, 5, 6]);

