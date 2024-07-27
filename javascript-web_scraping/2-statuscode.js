#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(`code: ${response.statusCode}`);
});
