#!/usr/bin/node

const dct = require('./101-data').dict;

const nwdct = {};
Object.keys(dct).map(function (key) {
  if (!Array.isArray(nwdct[dct[key]])) {
    nwdct[dct[key]] = [];
  }
  nwdct[dct[key]].push(key);
});
console.log(nwdct);
