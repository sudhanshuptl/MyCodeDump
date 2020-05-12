
const helpers = require("./helpers");
//import what you need
const {test} = require("./helpers2");
// varibales
//let : varible whose values change over time
// const: constant variable

// function is first class object 
 // so we can assign function to a variable 
const total = helpers.sum(10, 100);
const total_mult = helpers.mult(10,100);

console.log(helpers.greeting("Sudhanshu"));
console.log("Total Sum :", total);
console.log("Mult : ", total_mult);

console.log(test());
// console.log(helpers2.test2());