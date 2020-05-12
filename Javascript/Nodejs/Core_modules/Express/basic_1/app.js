const express = require("express");

// Initiate the app
const app = express()

// arg1 is route and arg 2 is handler function defined as array func
app.get('/', (req,res) => {
    res.send("Hello <br> Welcome to Express!!");
});


// localhost:4000
app.listen(4000);
