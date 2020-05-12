const fs = require("fs");

const fileName = "target.txt";

const errHandler = err => console.log("Error : ", err);
const dataHandler = data => console.log("Data : \n", data.toString());

fs.readFile(fileName, (err, data)=>{
    if (err) errHandler(err);
    dataHandler(data);
});

// This executed before file reading
console.log(" Node js Async programming")
