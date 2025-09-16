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

// 1

const colors = ["red", "green", "gray", "black", "white"];

// 2

for (let i = 0; i < colors.length; i++) {
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// 3

for (let i = 0; i < colors.length; i++) {
  console.log(`My ${i + 1}st choice is: ${colors[i]}`);
}

// Exercise 3

// 1
let userNumber = prompt("Enter a number: ");

// 2
if (typeof userNumber == "number") {
  while (userNumber < 10) {
    userNumber = prompt("Enter a new number: ");
  }
}

// Exercise 4

// 1
const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

// 2

console.log(building["numberOfFloors"]);

// 3

console.log(
  `Number of floors is first floor is ${building["numberOfAptByFloor"]["firstFloor"]}`
);
console.log(
  `Number of floors is thired floor is ${building["numberOfAptByFloor"]["thirdFloor"]}`
);

// 4

console.log(building["nameOfTenants"][1]);

console.log(
  building["numberOfRoomsAndRent"][
    building["nameOfTenants"][0].toLowerCase()
  ][0]
);

// 5

if (
  building["numberOfRoomsAndRent"]["david"] >
    building["numberOfRoomsAndRent"]["dan"] ||
  building["numberOfRoomsAndRent"]["sarah"] >
    building["numberOfRoomsAndRent"]["dan"]
)
  building["numberOfRoomsAndRent"]["dan"][1] = 1200;

// Exercise 5

// 1
const family = {
  number: 4,
  father: "ahmad",
  mother: "jamila",
};

// 2

for (fam in family) {
  console.log(fam);
}

// 3

for (fam in family) {
  console.log(family[fam]);
}

// Exercise 6

// 1

const details = {
  my: "name",
  is: "Rudolf",
  the: "reindeer",
};
let str = "";
for (let detail in details) {
  str += `${detail} ${details[detail]} `;
}
console.log(str);

// Exercise 7
// 1

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

names.sort();

let societyName = "";
for (let i = 0; i < names.length; i++) {
  societyName += names[i][0];
}

// 2
console.log(societyName);
