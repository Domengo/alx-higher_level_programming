#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

const newList = list.map((x, i) => x * 1);
console.log(newList);
