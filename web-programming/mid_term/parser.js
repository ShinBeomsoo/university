Array.prototype.multiIndexOf = function (el) {
  let idxs = [];
  for (let i = this.length - 1; i >= 0; i--) {
    if (this[i] === el) {
      idxs.unshift(i);
    }
  }
  return idxs;
};

function parser(scoreArray) {
  let harmonyArray = [];

  let start = scoreArray.multiIndexOf("(");
  let end = scoreArray.multiIndexOf(")");
  for (let i = 0; i < start.length; i++) {
    let harmony = scoreArray.slice(start[i] + 1, end[i]).join('');
    harmonyArray.push(harmony);
  }

  for (let i = 0; i < start.length; i++) {
    let start = scoreArray.multiIndexOf("(");
    let end = scoreArray.multiIndexOf(")");
    scoreArray.splice(start[0], end[0]-start[0]+1, harmonyArray[i]);
  }
  return scoreArray;
}
