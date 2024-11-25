#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.writeFile(filePath, 'Hello Node.js', 'utf8', (err) => {
  if (err) {
    return console.error(err);
  }
});
