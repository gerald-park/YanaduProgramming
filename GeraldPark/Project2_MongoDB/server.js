const { json } = require('express');
const express = require('express');
const app = express(); 
app.use(express.json())

const users = [];
app.get('/user',function(req,res){
    return res.send({users:users});
})

app.post('/user', function(req,res){
    users.push({name:req.body.name, age:req.body.age})
    return res.send({success: true})
})

app.listen(3004,function(){
    console.log("server linstening on port 3004")
})