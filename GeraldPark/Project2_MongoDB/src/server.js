const { json } = require("express");
const express = require("express");
const app = express();
const { userRouter, blogRouter } = require("./routes/");
const mongoose = require("mongoose");
const { generateFakeData } = require("../faker");
const MONGO_URI =
  "mongodb+srv://cyanluna:QQOevyzs0mpNlR1c@cluster0.e330g.mongodb.net/BlogService?retryWrites=true&w=majority";

const server = async () => {
  try {
    // await mongoose.connect(MONGO_URI, {
    //   useNewUrlParser: true,
    //   useUndifinedTopology: true,
    //   useCreateIndex: true,
    //   useFindAndModify: false,
    // });
    await mongoose.connect(MONGO_URI);
    //mongoose.set("debug", true);
    //generateFakeData(100, 10, 300);
    console.log("mongodb Connected");

    app.use(express.json());
    app.use("/user", userRouter);
    app.use("/blog", blogRouter);
    //app.use("/blog/:blogId/comment", commentRouter);

    app.listen(3004, () => console.log("server linstening on port 3004"));
  } catch (err) {
    console.log(err);
  }
};
server();
