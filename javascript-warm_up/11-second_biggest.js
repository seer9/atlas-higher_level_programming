#!/usr/bin/node

// automatically convert the arguments to numbers
const args = process.argv.slice(2).map(Number);
// check if there are fewer than 2 arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // sort the arguments in descending order then get the second biggest
  args.sort((a, b) => b - a);
  console.log(args[1]);
}