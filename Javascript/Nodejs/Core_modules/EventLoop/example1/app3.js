// syncronous
const fs = require("fs");

const fileName = "target.txt";

// sync method make the program syncrounous
// now program run sequencily 
const data = fs.readFileSync(fileName) 
console.log(data.toString());

// fs.readFileSync(fileName, (err, data)=>{
//     if (err){
//         console.log(err);
//     }
//     else{
//         console.log("file output :\n", data.toString());
//     }
// });

// This executed before file reading
console.log(" Node js Async programming")
