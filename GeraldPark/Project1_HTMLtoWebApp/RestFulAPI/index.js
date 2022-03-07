console.log("RestFulApiTest Learning NPM");

var express = require('express');
var app = express();
var router = require('./router.js')

app.use(express.json());
app.use(router);

app.listen(3000,function()
{
    console.log('RestFulApiTest 3000포트로 웹서버 실행!')
});

