
function sum(a, b){
    return a+b;
}


// Arrow function
const mult = (a,b) =>{
    return a*b;
}

// Array function does not their context
// So if you are using this inside it will use context of that file

// array function with single argument
const greeting = name => "Welcome " + name + "!!";

// array function with no argument
const greeting_all = () => "Welcome All"

console.log(greeting_all());

// add visibility globaly
module.exports = {
    sum,
    mult,
    greeting,
    greeting_all
};




//export is private to each module