console.log("Learning NPM");

var express = require('express');
var app = express();

app.use(function(req,res,next){
    res.send('ok');
})

app.listen(3000,function()
{
    console.log('3000포트로 웹서버 실행!')
});

