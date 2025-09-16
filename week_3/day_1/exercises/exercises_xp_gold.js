// ===== Exercise 1

let numbers = [123, 8409, 100053, 333333333, 7];

// 1
for (let i = 0; i < numbers.length; i++) {
  // 2
  console.log(numbers[i] % 3 === 0);
}

// ===== Exercise 2

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina",
};

// 1

let name = prompt("Enter your name");

// 2

if (guestList[name.toLowerCase()]) {
  console.log(
    `Hi! I'm ${name}, and I'm from ${guestList[name.toLowerCase()]}.`
  );
}
// 3
else {
  console.log("Hi! I'm a guest.");
}

// ===== Exercise 3

let age = [20, 5, 12, 43, 98, 55];

// 1
console.log(age.reduce((a, b) => a + b, 0));

// 2

console.log(Math.max(...age));
