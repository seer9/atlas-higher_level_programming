#!/usr/bin/node

// get the first and second arguments passed to the script
const arg1 = process.argv[2];
const arg2 = process.argv[3];
// c the arguments to integers
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);
// define the add function
function add (a, b) {
  return (a + b);
}
// check if the conversions were successful and print the result
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
