#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const completed = {};
  const tasks = JSON.parse(body);
  for (const i in tasks) {
    const task = tasks[i];
    if (task.completed === true) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});
