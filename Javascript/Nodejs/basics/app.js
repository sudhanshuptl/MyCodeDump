
const helpers = require("./helpers");

// varibales
//let : varible whose values change over time
// const: constant variable

// function is first class object 
 // so we can assign function to a variable 
const total = helpers.sum(10, 100);
const total_mult = helpers.mult(10,100);

console.log(helpers.greeting("Sudhanshu"))
console.log("Total Sum :", total);
console.log("Mult : ", total_mult);