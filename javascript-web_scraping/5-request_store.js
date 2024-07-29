#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length <= 2) {
  console.error('Usage: <api url> <file name>');
}

const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  fs.writeFile(`${fileName}`, body, 'utf-8', function (err) {
    if (err) {
      console.error(err);
    }
  });
});
