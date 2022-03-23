const express = require("express");
const { response } = require("express");
const { readFile } = require("fs");

const app = express()

app.get('/', (request, response) => {
   readFile('./index.html', 'utf8', (err, html) => {

      if (err) {
         response.status(500).send('Whoops something happended in our end!!! ')
      }

      response.send(html);

   }) 
});


app.listen(process.env.PORT || 3000, () => console.log('App can be used on http://localhost:3000'))
