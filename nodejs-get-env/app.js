const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.write('<h1>All Environment Variables:</h1>');
  res.write('<ul>');

  // Loop through all environment variables and display them
  for (let key in process.env) {
    res.write(`<li>${key}: ${process.env[key]}</li>`);
  }

  res.write('</ul>');
  res.end();
});

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
