#!/usr/bin/node

// get the first argument passed to the script, excluding the first two elements
const arg = process.argv[2];
// convert the argument to an integer
const num = parseInt(arg);
// factorial function
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
// print the factorial
console.log(factorial(num));
