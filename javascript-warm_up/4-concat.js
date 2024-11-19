#!/usr/bin/node

// exclude the first two arguments
const args = process.argv.slice(2);
// concatenate the first and second arguments using the concat method
const str = (args[0] || 'undefined').concat(' is ', args[1] || 'undefined');
// print the string
console.log(str);
