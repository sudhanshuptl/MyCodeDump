const express = require("express");

const app = express();

app.get("/", (req, res)=>{
    res.send("This is Home page")
});


// listen to port 40000
const port = 4000;
app.listen(port, ()=>{
    console.log(`Node js application is listning at port : ${port}`);
    
});
