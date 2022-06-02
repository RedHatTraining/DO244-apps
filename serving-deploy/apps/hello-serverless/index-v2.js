const http = require("http");
const userQuotas = require("./userQuotas");


http
    .createServer(requestHandler)
    .listen(3000, onListen);



function requestHandler(req, res) {
    res.writeHead(
        200,
        { "Content-Type": "application/json" }
    );

    formattedValues = format(userQuotas.all())

    res.end(JSON.stringify(formattedValues));
}


function format(userQuotas) {
    return Object
        .keys(userQuotas)
        .map(userId => userQuotas[userId].toFixed(4));
}


function onListen() {
    console.info("Server listening at port 3000");
}
