#!/usr/bin/node

const { argv } = require('process');
const x = argv[2];

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    let row = '';
    for (let j = 0; j < parseInt(x); j++) {
      row += 'X';
    }
    console.log(row);
  }
}
