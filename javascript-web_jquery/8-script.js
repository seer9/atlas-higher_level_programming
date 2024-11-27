#!/usr/bin/node
/* global $ */

$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const movies = data.results;
    movies.forEach(movie => {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
