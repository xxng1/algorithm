const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
    a = input[0];
    b = input[1];
    console.log("a =",a);
    console.log("b =",b);
}).on('close', function () {
    // console.log(Number(input[0]) + Number(input[1]));
});