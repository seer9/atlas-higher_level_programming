#!/usr/bin/node

// slice() to exclude the first two elements/arguements
const args = process.argv.slice(2);
// concatenate the first and second arguements properly
const str = args[0].concat(' is ', args[1]);
// print the string
console.log(str);
