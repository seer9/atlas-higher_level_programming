#!/usr/bin/node

// get the first argument passed to the script
const arg = process.argv[2];
// convert the argument to an integer
const num = parseInt(arg);
// check if the conversion was successful
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  // Loop to print "C is fun" num times
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
