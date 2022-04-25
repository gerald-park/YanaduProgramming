const { Router } = require('express');
const userRouter = Router();
const { User } = require('../models/User');
const mongoose = require('mongoose');

userRouter.get('/', async (req,res) => {
    try{
        const users = await User.find({});
        return res.send({users:users});
    }catch(err){
        console.log(err);
        return res.status(500).send({err: err.message})
    }
})
userRouter.get('/:userId', async (req,res) => {
    console.log(req.params);
    try{
        const { userId } = req.params; 
        if(!mongoose.isValidObjectId(userId)) return res.status(400).send("err : Invaild userId");
        const user = await User.findOne({ _id: userId });
        return res.send({ user });
    }catch(err){
        console.log(err);
        return res.status(500).send({err: err.message});
    }
})
userRouter.post('/', async (req,res) => {
    try{
        let {username, name} = req.body;
        if(!username) return res.status(400).send({err: "username is required"}); // 잘못된 요청 처리
        if(!name || !name.first || !name.last) return res.status(400).send({ err : "both first and last names are required"})
        const user = new User(req.body);
        await user.save();
        return res.send({ user })        
    }catch(err){
        console.log(err);
        return res.status(500).send({err: err.message}); // 실패 에러 메시지
    }
})
userRouter.delete('/:userId', async(req,res) => {
    try{
        const { userId } = req.params;
        if(!mongoose.isValidObjectId(userId)) return res.status(400).send("err : Invaild userId");
        const user = await User.findOneAndDelete({_id: userId })
        return res.send({ user });
    }catch(err){
        console.log(err);
        return res.status(500).send({err: err.message});
    }
})
//Update User
userRouter.put('/:userId', async(req,res) => { 
    try{
        const { userId } = req.params;
        if(!mongoose.isValidObjectId(userId)) return res.status(400).send("err : Invaild userId");
        const { age, name } = req.body;
        if(!age && !name) return res.status(400).send({err:"age or name is requried"});
        if(typeof age !== 'number') return res.status(400).send({err: "age is must be a number"});
        if(name && typeof name.first !== 'string' && typeof name.last !== 'string') return res.status(400).send({err: "first and last name are must be string"});
        
        let updateBody = {};
        if(age) updateBody.age = age;
        if(name) updateBody.name = name;
        
        const user = await User.findByIdAndUpdate( userId,  updateBody, {new : true});
        return res.send({ user });
    }catch(err){
        console.log(err);
        return res.status(500).send({err: err.message});
    }
})

module.exports = {
    userRouter
}