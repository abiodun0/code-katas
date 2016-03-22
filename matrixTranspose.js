
// # print transpose_rows([[1,2,3,4],
// #                       [2,3,1,3],
// #                       [3,1,2,3]])`
// # This should return `[[1,2,3],
// #                       [2,3,1],
// #                       [3,1,2],[4,3,3]```
// # (edited)

// # [1:44]
// #  ```print transpose_rows([['cricket', 'football', 'tennis'], ['golf']])
// # This should return `[['cricket',golf'],
// #                       ['football'],
// #                       ['golf']


transpose = function(a) {

  // Calculate the width and height of the Array
  var w = a.length ? a.length : 0,
    h = a[0] instanceof Array ? a[0].length : 0;

  // In case it is a zero matrix, no transpose routine needed.
  if(h === 0 || w === 0) { return []; }

  /**
   * @var {Number} i Counter
   * @var {Number} j Counter
   * @var {Array} t Transposed data is stored in this array.
   */
  var i, j, t = [];

  // Loop through every item in the outer array (height)
  for(i=0; i<h; i++) {

    // Insert a new row (array)
    t[i] = [];

    // Loop through every item per item in outer array (width)
    for(j=0; j<w; j++) {

      // Save transposed data.
      if(a[j][i] !== undefined) t[i][j] = a[j][i];
    }
  }

  return t;
};
console.log(transpose([[1,2,3,4],[2,3,1,3],[3,1,2,3]]));
console.log(transpose([['cricket', 'football', 'tennis'], ['golf']]))