const http = require("http");

const version = "v2";

function requestHandler(req, res) {
  res.writeHead(200);
  res.end(`Hello ${version}!`);
}

const server = http.createServer(requestHandler);
server.listen(8080, () => {
    console.log("Server listening on port 8080");
});
