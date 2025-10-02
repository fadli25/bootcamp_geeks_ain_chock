// Exercise 1 : Random Number
let random = Math.floor(Math.random() * 100) + 1;
for (let i = 0; i <= random; i++) {
  if (i % 2 === 0) console.log(i);
}

// Exercise 2 : Capitalized letters
function capitalize(str) {
  let even = "";
  let odd = "";
  for (let i = 0; i < str.length; i++) {
    if (i % 2 === 0) {
      even += str[i].toUpperCase();
      odd += str[i];
    } else {
      even += str[i];
      odd += str[i].toUpperCase();
    }
  }
  return [even, odd];
}
console.log(capitalize("abcdef"));

// Exercise 3 : Is palindrome?
function isPalindrome(str) {
  return str === str.split("").reverse().join("");
}
console.log(isPalindrome("madam"));
console.log(isPalindrome("hello"));

// Exercise 4 : Biggest Number
function biggestNumberInArray(arr) {
  let nums = arr.filter((x) => typeof x === "number");
  if (nums.length === 0) return 0;
  return Math.max(...nums);
}
console.log(biggestNumberInArray([-1, 0, 3, 100, 99, 2, 99])); // 100
console.log(biggestNumberInArray(["a", 3, 4, 2])); // 4
console.log(biggestNumberInArray([])); // 0

// Exercise 5 : Unique Elements
function unique(arr) {
  return [...new Set(arr)];
}
console.log(unique([1, 2, 3, 3, 3, 3, 4, 5])); // [1,2,3,4,5]

// Exercise 6 : Calendar
function createCalendar(year, month) {
  let mon = month - 1;
  let d = new Date(year, mon);
  let table = document.createElement("table");

  let weekdays = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"];
  let headerRow = document.createElement("tr");
  weekdays.forEach((day) => {
    let th = document.createElement("th");
    th.textContent = day;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  let row = document.createElement("tr");
  for (let i = 0; i < (d.getDay() + 6) % 7; i++) {
    row.appendChild(document.createElement("td"));
  }

  while (d.getMonth() === mon) {
    let td = document.createElement("td");
    td.textContent = d.getDate();
    row.appendChild(td);
    if (d.getDay() === 0) {
      table.appendChild(row);
      row = document.createElement("tr");
    }
    d.setDate(d.getDate() + 1);
  }

  if (row.children.length > 0) table.appendChild(row);
  document.body.appendChild(table);
}
createCalendar(2012, 9);
