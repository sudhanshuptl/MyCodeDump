const express = require("express");

const postController = require("../controller/post");

router = express.Router();

//map routes
router.get('/', postController.getPosts)

module.exports = router;