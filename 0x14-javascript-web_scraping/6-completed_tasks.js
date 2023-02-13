#!/usr/bin/node

const request = require('request');
const { json } = require('stream/consumers');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (err, response, body) => {
    if (err) {
        console.log(err);
    }
    const completed = {};
    const json = JSON.parse(body);
    for (const i in json) {
        const task = json[i];
        if (task.completed == true) {
            if (completed[task.userId] === undefined) {
                completed[task.userId] = 1;
            }
        }
    
    }
    console.log(completed);
});