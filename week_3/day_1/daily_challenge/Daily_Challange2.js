let n = 5;
let output = "";
let count = 0;
let starsInRow = 1;

for (let i = 1; i <= (n * (n + 1)) / 2; i++) {
  output += "* ";
  count++;

  if (count === starsInRow) {
    output += "\n";
    starsInRow++;
    count = 0;
  }
}

console.log(output);

for (let i = 0; i < 5; i++) {
  let str = "";
  for (let j = 0; j <= i; j++) {
    str += "* ";
  }
  console.log(str);
}
