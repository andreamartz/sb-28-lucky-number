function starOutGrid(grid) {
  // starLocations is an array of sets
  const starLocations = findStars(grid);

  // we want to turn those sets in starLocations back into arrays
  rowsArr = Array.from(starLocations[0]);
  colsArr = Array.from(starLocations[1]);
  
  // if there are no asterisks in the grid, return it unchanged
  if (rowsArr.length === 0 && colsArr.length === 0) {
    return grid;
  }
  
  for (const rowIdx of rowsArr) {
    // for rows containing an asterisk, fill the whole row with asterisks
    for (i = 0; i < grid[rowIdx].length; i++) {
      grid[rowIdx][i] = '*';
    }
  }    

  for (const colIdx of colsArr) {
    // for cols containing an asterisk, make the whole column asterisks
    for (const row of grid) {
      row[colIdx] = '*';
    }
  }

  // console.log('changed col(s):', grid);
  return grid;
}

function findStars(grid) {
  // rows and cols will eventually contain the row and column indices respectively where asterisks exist in grid
  let rows = [];
  let cols = [];
  for (i = 0; i < grid.length; i++) {
    for (j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === '*') {
        rows.push(i);
        cols.push(j);
      }
    }
  }
  // turn rows and cols array into sets to remove dupe values
  rowsSet = new Set(rows);
  colsSet = new Set(cols);

  starLocations = [rowsSet, colsSet];
  return starLocations;
}
