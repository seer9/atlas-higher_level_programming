#!/usr/bin/node

// slice() excludes the first two elements so it
// only counts the passed arguements
const args = process.argv.slice(2);

// printing using log() method
console.log(args[0]
  ? args[0]
  : 'No argument');
