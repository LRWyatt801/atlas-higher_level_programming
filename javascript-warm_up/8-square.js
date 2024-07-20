#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  for (let height = 0; height < size; height++) {
    let row = '';
    for (let width = 0; width < size; width++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
