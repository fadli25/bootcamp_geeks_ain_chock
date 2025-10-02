// Exercise 1

// #1
function funcOne() {
  let a = 5;
  if (a > 1) {
    a = 3;
  }
  alert(`inside the funcOne function ${a}`); // 3
}
// #1.2 If const instead of let, error if you try to reassign a inside if block

// #2
let a = 0;
function funcTwo() {
  a = 5; // modifies the global 'a'
}
function funcThree() {
  alert(`inside the funcThree function ${a}`);
}
// #2.1
funcThree(); // 0
funcTwo();
funcThree(); // 5
// #2.2 If const, funcTwo would throw an error because const cannot be reassigned

// #3
function funcFour() {
  window.a = "hello"; // creates global variable on window object
}
function funcFive() {
  alert(`inside the funcFive function ${a}`); // hello
}
// #3.1
funcFour();
funcFive();

// #4
let a = 1;
function funcSix() {
  let a = "test";
  alert(`inside the funcSix function ${a}`); // test (local)
}
// #4.1
funcSix();
// #4.2 const works same as let for local scope, cannot reassign

// #5
let a = 2;
if (true) {
  let a = 5;
  alert(`in the if block ${a}`); // 5
}
alert(`outside of the if block ${a}`); // 2
// #5.2 const instead of let works same, cannot reassign inside block

// Exercise 2

const winBattle = () => true;

const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints); // 10

// Exercise 3

const isString = (value) => typeof value === "string";

console.log(isString("hello")); // true
console.log(isString([1, 2, 4, 0])); // false

// Exercise 4

const sum = (a, b) => a + b;
console.log(sum(5, 10)); // 15

// Exercise 5

// Function declaration
function kgToGrams(kg) {
  return kg * 1000;
}
console.log(kgToGrams(2)); // 2000

// Function expression
const kgToGramsExpr = function (kg) {
  return kg * 1000;
};
console.log(kgToGramsExpr(3)); // 3000

// Function declaration vs expression: Declarations are hoisted, expressions are not

// Arrow function
const kgToGramsArrow = (kg) => kg * 1000;
console.log(kgToGramsArrow(4)); // 4000

// Exercise 6

(function (children, partner, location, job) {
  const msg = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids.`;
  document.body.innerHTML += `<p>${msg}</p>`;
})(3, "Alice", "Paris", "Engineer");

// Exercise 7

(function (userName) {
  const navbar = document.querySelector("nav");
  const div = document.createElement("div");
  div.innerHTML = `<img src="profile.jpg" alt="Profile" width="30" height="30"> ${userName}`;
  navbar.appendChild(div);
})("John");

// Exercise 8

// Part I
function makeJuice(size) {
  function addIngredients(ing1, ing2, ing3) {
    document.body.innerHTML += `<p>The client wants a ${size} juice containing ${ing1}, ${ing2}, ${ing3}.</p>`;
  }
  addIngredients("apple", "banana", "orange");
}
makeJuice("large");

// Part II
function makeJuice(size) {
  const ingredients = [];
  function addIngredients(ing1, ing2, ing3) {
    ingredients.push(ing1, ing2, ing3);
  }
  function displayJuice() {
    document.body.innerHTML += `<p>The client wants a ${size} juice containing ${ingredients.join(
      ", "
    )}.</p>`;
  }
  addIngredients("apple", "banana", "orange");
  addIngredients("mango", "pineapple", "kiwi");
  displayJuice();
}
makeJuice("large");
