//  Exercise 1
function displayNumbersDivisible(divisor = 23) {
  let sum = 0;
  for (let i = 0; i <= 500; i++) {
    if (i % divisor === 0) {
      console.log(i);
      sum += i;
    }
  }
  console.log("Sum:", sum);
}
displayNumbersDivisible();
displayNumbersDivisible(3);
displayNumbersDivisible(45);

//  Exercise 2
const stock = { banana: 6, apple: 0, pear: 12, orange: 32, blueberry: 1 };
const prices = { banana: 4, apple: 2, pear: 1, orange: 1.5, blueberry: 10 };
const shoppingList = ["banana", "orange", "apple"];

function myBill() {
  let total = 0;
  for (let item of shoppingList) {
    if (item in stock && stock[item] > 0) {
      total += prices[item];
      stock[item]--;
    }
  }
  return total;
}
console.log(myBill());

// Exercise 3
function changeEnough(itemPrice, amountOfChange) {
  const values = [0.25, 0.1, 0.05, 0.01];
  let total = 0;
  for (let i = 0; i < amountOfChange.length; i++) {
    total += amountOfChange[i] * values[i];
  }
  return total >= itemPrice;
}
console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2, 100, 0, 0]));
console.log(changeEnough(0.75, [0, 0, 20, 5]));

//  Exercise 4
function hotelCost(nights) {
  return nights * 140;
}
function planeRideCost(destination) {
  if (destination === "London") return 183;
  if (destination === "Paris") return 220;
  return 300;
}
function rentalCarCost(days) {
  let cost = days * 40;
  if (days > 10) cost *= 0.95;
  return cost;
}
function totalVacationCost(nights, destination, days) {
  const hotel = hotelCost(nights);
  const plane = planeRideCost(destination);
  const car = rentalCarCost(days);
  return `The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}`;
}
console.log(totalVacationCost(5, "Paris", 12));

//  Exercise 5
const div = document.querySelector("div");
console.log(div);
document.querySelectorAll("ul")[0].children[1].textContent = "Richard";
document.querySelectorAll("ul")[1].children[1].remove();
document
  .querySelectorAll("ul")
  .forEach((ul) => (ul.children[0].textContent = "Zakaria"));
document
  .querySelectorAll("ul")
  .forEach((ul) => ul.classList.add("student_list"));
document.querySelectorAll("ul")[0].classList.add("university", "attendance");
div.style.backgroundColor = "lightblue";
div.style.padding = "20px";
document.querySelectorAll("ul")[1].lastElementChild.style.display = "none";
document.querySelectorAll("ul")[0].children[1].style.border = "1px solid black";
document.body.style.fontSize = "20px";
if (div.style.backgroundColor === "lightblue") {
  alert("Hello John and Pete");
}

//  Exercise 6
const nav = document.getElementById("navBar");
nav.setAttribute("id", "socialNetworkNavigation");
const newLi = document.createElement("li");
const text = document.createTextNode("Logout");
newLi.appendChild(text);
nav.querySelector("ul").appendChild(newLi);
console.log(nav.querySelector("ul").firstElementChild.textContent);
console.log(nav.querySelector("ul").lastElementChild.textContent);

//  Exercise 7
const allBooks = [
  {
    title: "Harry Potter",
    author: "J.K. Rowling",
    image: "https://picsum.photos/100",
    alreadyRead: true,
  },
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image: "https://picsum.photos/101",
    alreadyRead: false,
  },
];
const section = document.querySelector(".listBooks");
allBooks.forEach((book) => {
  const div = document.createElement("div");
  div.innerHTML = `${book.title} written by ${book.author}`;
  const img = document.createElement("img");
  img.src = book.image;
  img.style.width = "100px";
  div.appendChild(img);
  if (book.alreadyRead) div.style.color = "red";
  section.appendChild(div);
});
