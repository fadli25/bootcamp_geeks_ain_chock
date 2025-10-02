let input = prompt("Enter several words separated by commas:");
let words = input.split(",").map((w) => w.trim());

let maxLength = Math.max(...words.map((w) => w.length));
let border = "*".repeat(maxLength + 4);

console.log(border);
for (let word of words) {
  console.log(`* ${word}${" ".repeat(maxLength - word.length)} *`);
}
console.log(border);
