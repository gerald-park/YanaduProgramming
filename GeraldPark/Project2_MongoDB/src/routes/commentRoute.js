const { Router } = require("express");
const commentRouter = Router({ mergeParams: true });
const { Comment } = require("../models/Comment");
const { Blog } = require("../models/Blog");
const { User } = require("../models/User");
const { isValidObjectId } = require("mongoose");
/*
    /user
    /blog
    /comment : 얘는 단독 호출이 안됨 -> /blog/:blogId/comment 이렇게 호출하는게 바람직함 
*/
commentRouter.post("/", async (req, res) => {
  try {
    const { blogId } = req.params;
    const { content, userId } = req.body;
    if (!isValidObjectId(blogId))
      return res.status(400).send({ err: "blogId is invalid" });
    if (!isValidObjectId(userId))
      return res.status(400).send({ err: "userId is invalid" });
    if (typeof content !== "string")
      return res.status(400).send({ err: "content is required" });

    // const blog = await Blog.findByIdAndUpdate(blogId);
    // const user = await User.findByIdAndUpdate(userId);
    const [blog, user] = await Promise.all([
      Blog.findByIdAndUpdate(blogId),
      User.findByIdAndUpdate(userId),
    ]);

    if (!blog || !user)
      return res.status(400).send({ err: " blog or user doesn't not exist" });
    if (!blog.islive) res.status(400).send({ err: "blog is not availbe" });
    const comment = new Comment({ content, user, blog });
    return res.send({ comment });
  } catch (err) {
    return res.status(400).send({ err: err.message });
  }
});
commentRouter.get("/");

module.exports = { commentRouter };
