#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(file, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
  console.log(`The string was written to ${file}`);
});
