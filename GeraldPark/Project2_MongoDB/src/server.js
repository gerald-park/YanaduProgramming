const { json } = require('express');
const express = require('express');
const app = express(); 
const mongoose = require('mongoose');
const { User } = require('./models/User');

const MONGO_URI = 'mongodb+srv://cyanluna:QQOevyzs0mpNlR1c@cluster0.e330g.mongodb.net/BlogService?retryWrites=true&w=majority'

const server = async () => {
    try{
        await mongoose.connect(MONGO_URI);
        console.log('mongodb Connected');

        app.use(express.json());

        app.get('/user', async (req,res) => {
            try{
                const users = await User.find({});
                return res.send({users:users});
            }catch(err){
                console.log(err);
                return res.status(500).send({err: err.message})
            }
        })
        
        app.post('/user', async (req,res) => {
            try{
                let {username, name} = req.body;
                if(!username) return res.status(400).send({err: "username is required"}); // 잘못된 요청 처리
                if(!name || !name.first || !name.last) return res.status(400).send({ err : "both first and last names are required"})
                const user = new User(req.body);
                await user.save();
                return res.send({ user })        
            }catch(err){
                console.log(err)
                return res.status(500).send({err: err.message}); // 실패 에러 메시지
            }
        })
        app.listen(3004,() => console.log("server linstening on port 3004"))
    } catch(err){
        console.log(err);
    }
}
server();