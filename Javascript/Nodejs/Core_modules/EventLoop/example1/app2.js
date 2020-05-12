//asyncronous
const fs = require("fs");

const fileName = "target.txt";



fs.readFile(fileName, (err, data)=>{
    if (err){
        console.log(err);
    }
    else{
        console.log("file output :\n", data.toString());
    }
});

// This executed before file reading
console.log(" Node js Async programming")
