const http = require('node:http');
const hostname = '127.0.0.1';
const port = 8080;
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World1 \n');
  alert("hi");
  res.write(req.url);
  res.end();
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
  console.log('Hello')
});