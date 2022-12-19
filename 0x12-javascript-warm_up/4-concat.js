#!/usr/bin/node

const { argv } = require('process');
const conj = 'is';
argv.forEach((argv, conj) => {
  console.log(argv[3] + conj + argv[4]);
});
