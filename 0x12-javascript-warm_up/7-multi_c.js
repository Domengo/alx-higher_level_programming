#!/usr/bin/node
const { argv } = require('process');
const x = argv[2];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
}
