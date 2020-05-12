const fs = require("fs"); //file handling

const fileName = 'target.txt';

// watch target.txt for any changes
// argument 1  is file name 
//argument 2 is callback function
fs.watch(fileName, ()=>{
    console.log(" File changed !! :P")
})