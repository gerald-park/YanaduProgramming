const express = require('express');
const app = express(); 

app.get('/',function(req,res){
    return res.send('hello world- nondemon');
})

app.listen(3004,function(){
    console.log("server linstening on port 3004")
})