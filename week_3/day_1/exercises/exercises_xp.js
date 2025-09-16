// ===== Exercise 1

const people = ["Greg", "Mary", "Devon", "James"];

// 1
people.shift();

// 2
people[3] = "Jason";

// 3
people.push("Zakaria");

// 4
console.log(people.indexOf("Mary"));

// 5
let newPeople = people.slice(1, 4);

// 6
console.log(people.indexOf("Foo")); // -1

// becuase "Foo" is not in the array

// 7
let last = people[people.length - 1];

// the reason we use people.length - 1 is because the index starts at 0

// Part II - Loops

// 1
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

// 2

for (let i = 0; i < people.length; i++) {
  if (people[i] === "Devon") {
    break;
  }
  console.log(people[i]);
}

// ===== Exercise 2
