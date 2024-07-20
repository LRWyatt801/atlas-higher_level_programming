#!/usr/bin/node
const args = process.argv.slice(2);
let output;
if (args.length === 0) {
  output = 'No argument';
} else if (args.length === 1) {
  output = 'Argument found';
} else {
  output = 'Arguments found';
}
console.log(output);
