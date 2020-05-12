const http = require('http');

// create a web server
const server  = http.createServer(
    (req, resp) => {
        resp.end("Hello world from nodejs updated")
    }
)

//start lisning for request
console.log("start : http://localhost:4000/")
server.listen(4000);
// open : http://localhost:4000/