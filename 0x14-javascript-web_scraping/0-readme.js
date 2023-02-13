#!/usr/bin/node

const fs = require('fs');
file = process.argv[1];

fs.readFile(file, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});