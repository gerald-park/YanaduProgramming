var http = require('http');
var express = require('express');
var app = express();
const cros = require('cors');

app.use(express.json());
app.use(express.static("public"));
app.use(cros());

var todos = {"자바스크립트공부하기": true};

app.listen(3000, function() {
    console.log("App listening on port 3000!");
});

app.post("/todos", function(req, res) {
 todos = req.body.todos;
 console.log(req.body);
 res.status(200).send({message : "success"});
 console.log("post : " + todos);
});

app.get("/todos", function(req, res) {
    res.status(200).send(todos);
    console.log("get : " + todos);
});
