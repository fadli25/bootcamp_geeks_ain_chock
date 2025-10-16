const { persons } = require("./data.js");

const ages = persons.map((x) => x.age);

const avg = ages.some() / ages.length;

console.log(avg);
