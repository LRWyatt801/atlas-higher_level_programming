#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

Object.defineProperty(myObject, 'value', { value: 89 });

console.log(myObject);
