const { products } = require("./products.js");

function search(name) {
  return products.filter((x) => x.name === name)[0];
}

console.log(search("BMW"));

console.log(search("Dacia"));
