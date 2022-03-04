
var express = require("express");
var request = require("request");
const cors = require('cors');

var app = express();

var messages = [];

app.use(express.json());
app.use(express.static("public"));
app.use(cors());

app.listen(3000, function(){
    console.log("Chat App listening on poert 3000")
});

app.post('/send', function(req, res){
    var message = {
        sender: req.body.sender,
        ko: req.body.ko,
        en: req.body.en
    };
    console.log(message);
    console.log(message.ko.length  + ' ' + message.en.length)
    var options = {
        url : "https://openapi.naver.com/v1/papago/n2mt",
        form:{
            source : message.ko.length == 0 ? "en" : "ko",
            target : message.ko.length == 0 ? "ko" : "en",
            text: message.ko.length == 0 ? message.en : message.ko
        },
        headers : {
            "X-Naver-Client-Id": "m7lEO63BjdjfX1ibYTYS",
            "X-Naver-Client-Secret": "fqMGEPfkt4",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
    };
    console.log(options)
    request.post(options, function(error, respose){
        console.log(JSON.parse(respose.body));
        var result = JSON.parse(respose.body).message.result;
        message.ko = message.ko.length == 0 ? result.translatedText : message.ko;
        message.en = message.en.length == 0 ? result.translatedText : message.en;
        console.log(message);
        messages.push(message);
        res.status(200).send({ message: "Success" });
    });
});

app.get("/receive", function(req,res){
    var result = { total: messages.length, messages : [] };
    if(messages.length > req.query.from){
        result.messages = messages.slice(req.query.from);
    }
    res.status(200).send(result);
})