const express = require('express');
const app = express();
const http = require('http').Server(app);
const path = require('path');

const PORT = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'client')));

app.listen(PORT, () => {
  console.log('Waiting for connections on port ::: ' + PORT);
});