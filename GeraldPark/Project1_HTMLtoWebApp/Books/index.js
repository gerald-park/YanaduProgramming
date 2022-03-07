console.log("Books Learning NPM");

var express = require('express');
var app = express();
var router = require('./router.js')
var booksRouter = require('./books.js')

app.use(express.json());
app.use(express.static('public'))
app.use('/router', router);
app.use('/books', booksRouter)

app.listen(3000,function()
{
    console.log('Books 3000포트로 웹서버 실행!')
});

