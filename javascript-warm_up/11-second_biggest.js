#!/usr/bin/node
// check for no arguments or just one
if (process.argv.length <= 2) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(arg => parseInt(arg));
  // sort the array in descending order
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
