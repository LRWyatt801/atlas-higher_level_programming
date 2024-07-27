#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.error('Usage: ./3-starwars_title.js <movie id>');
}

const titleId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${titleId}`;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const title = JSON.parse(body).title;
  console.log(title);
});
