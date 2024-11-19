#!/usr/bin/node

// get the first argument passed to the script, excluding the first two elements
const arg = process.argv[2];
// convert the argument to an integer
const size = parseInt(arg);
// check if the conversion was successful
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // loop to print the square
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
