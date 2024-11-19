#!/usr/bin/node

// get the first argument passed to the script,
// excluding the first two elements
const arg = process.argv[2];

// convert the argument to an integer
const num = parseInt(arg);

// check if the conversion was successful and
// print the appropriate message
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
