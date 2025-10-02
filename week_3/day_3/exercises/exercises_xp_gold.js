// Exercise 1 : is_Blank
function isBlank(str) {
  return str.trim() === "";
}
console.log(isBlank("")); // true
console.log(isBlank("abc")); // false

// Exercise 2 : Abbrev_name
function abbrevName(name) {
  let parts = name.split(" ");
  return parts[0] + " " + parts[1][0] + ".";
}
console.log(abbrevName("Robin Singh")); // "Robin S."

// Exercise 3 : SwapCase
function swapCase(str) {
  return str
    .split("")
    .map((ch) =>
      ch === ch.toUpperCase() ? ch.toLowerCase() : ch.toUpperCase()
    )
    .join("");
}
console.log(swapCase("The Quick Brown Fox")); // "tHE qUICK bROWN fOX"

// Exercise 4 : Omnipresent value
function isOmnipresent(arr, val) {
  return arr.every((sub) => sub.includes(val));
}
console.log(
  isOmnipresent(
    [
      [1, 1],
      [1, 3],
      [5, 1],
      [6, 1],
    ],
    1
  )
); // true
console.log(
  isOmnipresent(
    [
      [1, 1],
      [1, 3],
      [5, 1],
      [6, 1],
    ],
    6
  )
); // false

// Exercise 5 : Red Table

// <!DOCTYPE HTML>
// <html>
// <head>
//   <style>
//     table { border-collapse: collapse; }
//     td { border: 1px solid black; padding: 3px 5px; }
//   </style>
// </head>
// <body>
//   <table>
//     <tr><td>1:1</td><td>2:1</td><td>3:1</td><td>4:1</td><td>5:1</td></tr>
//     <tr><td>1:2</td><td>2:2</td><td>3:2</td><td>4:2</td><td>5:2</td></tr>
//     <tr><td>1:3</td><td>2:3</td><td>3:3</td><td>4:3</td><td>5:3</td></tr>
//     <tr><td>1:4</td><td>2:4</td><td>3:4</td><td>4:4</td><td>5:4</td></tr>
//     <tr><td>1:5</td><td>2:5</td><td>3:5</td><td>4:5</td><td>5:5</td></tr>
//   </table>
//   <script>
//     let table = document.querySelector("table");
//     for (let i = 0; i < table.rows.length; i++) {
//       table.rows[i].cells[i].style.backgroundColor = "red";
//     }
//   </script>
// </body>
// </html>
