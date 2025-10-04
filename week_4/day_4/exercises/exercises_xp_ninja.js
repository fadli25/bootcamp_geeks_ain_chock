// Exercise 1 : Dog age to Human years

const data = [
  { name: "Butters", age: 3, type: "dog" },
  { name: "Cuty", age: 5, type: "rabbit" },
  { name: "Lizzy", age: 6, type: "dog" },
  { name: "Red", age: 1, type: "cat" },
  { name: "Joey", age: 3, type: "dog" },
  { name: "Rex", age: 10, type: "dog" },
];

// Using a loop
let sumDogYears = 0;
for (let i = 0; i < data.length; i++) {
  if (data[i].type === "dog") {
    sumDogYears += data[i].age * 7; // 1 dog year = 7 human years
  }
}
console.log(sumDogYears);
// Output: 182

// Using reduce
const sumDogYearsReduce = data.reduce((acc, curr) => {
  if (curr.type === "dog") {
    return acc + curr.age * 7;
  }
  return acc;
}, 0);
console.log(sumDogYearsReduce);
// Output: 182

// Exercise 2 : Email
const userEmail3 = " cannotfillemailformcorrectly@gmail.com ";
const cleanedEmail = userEmail3.trim();
console.log(cleanedEmail);
// Output: 'cannotfillemailformcorrectly@gmail.com'

// Exercise 3 : Employees #3
const users = [
  { firstName: "Bradley", lastName: "Bouley", role: "Full Stack Resident" },
  { firstName: "Chloe", lastName: "Alnaji", role: "Full Stack Resident" },
  { firstName: "Jonathan", lastName: "Baughn", role: "Enterprise Instructor" },
  { firstName: "Michael", lastName: "Herman", role: "Lead Instructor" },
  { firstName: "Robert", lastName: "Hajek", role: "Full Stack Resident" },
  { firstName: "Wes", lastName: "Reid", role: "Instructor" },
  { firstName: "Zach", lastName: "Klabunde", role: "Instructor" },
];

const usersObj = {};
users.forEach((user) => {
  usersObj[`${user.firstName} ${user.lastName}`] = user.role;
});
console.log(usersObj);
/* Output:
{
  "Bradley Bouley": "Full Stack Resident",
  "Chloe Alnaji": "Full Stack Resident",
  "Jonathan Baughn": "Enterprise Instructor",
  "Michael Herman": "Lead Instructor",
  "Robert Hajek": "Full Stack Resident",
  "Wes Reid": "Instructor",
  "Zach Klabunde": "Instructor"
}
*/

// Exercise 4 : Array to Object
const letters = ["x", "y", "z", "z"];

// Using a for loop
const countObj = {};
for (let i = 0; i < letters.length; i++) {
  const letter = letters[i];
  countObj[letter] = (countObj[letter] || 0) + 1;
}
console.log(countObj);
// Output: { x: 1, y: 1, z: 2 }

// Using reduce
const countObjReduce = letters.reduce((acc, curr) => {
  acc[curr] = (acc[curr] || 0) + 1;
  return acc;
}, {});
console.log(countObjReduce);
// Output: { x: 1, y: 1, z: 2 }
