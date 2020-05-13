const express = require("express");
const morgan = require("morgan")

const getPosts = require("./routs/post")

const app = express();

//middleware
// dev for developent mode
//  this middleware log api requirest details in log
app.use(morgan("dev"))

// create personal middleware
const myPersonalMiddleware = (req, res, next)=> {
    console.log("Personal Middleware test");
    next(); // pass the control to next event  else program will stuck here
}

//app.use(myPersonalMiddleware);

// we can use middleware to check authentication
//app.get("/", checkAuth ,getPosts);

//app.get("/", getPosts);

app.use("/", getPosts)

// listen to port 40000
const port = 4000;
app.listen(port, ()=>{
    console.log(`Node js application is listning at port : ${port}`);
    
});
