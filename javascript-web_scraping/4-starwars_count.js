#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.error('Usage: ./3-starwars_title.js <api url>');
}

const apiurl = process.argv[2];

request(apiurl, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  let filmCount = 0;
  const films = JSON.parse(body);
  for (const film of films.results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        filmCount++;
      }
    }
  }
  console.log(filmCount);
});
