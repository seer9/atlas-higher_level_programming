#!/usr/bin/node

// only counts the passed arguements
const args = process.argv.length - 2;

// printing using log() method
console.log(
  args === 0
    ? 'No argument'
    : args === 1
      ? 'Argument found'
      : 'Arguments found');
