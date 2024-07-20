#!/usr/bin/node
function factorial (total, a) {
  return (total * a);
}

const num = parseInt(process.argv[2]);
if (num !== 1) {
  let total = 1;
  for (let i = 1; i <= num; i++) {
    total = factorial(total, i);
  }
  console.log(total);
}
