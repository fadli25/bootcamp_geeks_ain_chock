// ===== Exercise 1

// 1. Retrieve the h1 and log it
const h1 = document.querySelector("article h1");
console.log(h1);

// 2. Remove the last paragraph
const article = document.querySelector("article");
article.removeChild(article.lastElementChild);

// 3. Change background of h2 on click
const h2 = document.querySelector("article h2");
h2.addEventListener("click", () => {
  h2.style.backgroundColor = "red";
});

// 4. Hide h3 on click
const h3 = document.querySelector("article h3");
h3.addEventListener("click", () => {
  h3.style.display = "none";
});

// 5. Button to make paragraphs bold
const btn = document.createElement("button");
btn.innerText = "Make paragraphs bold";
document.body.appendChild(btn);

btn.addEventListener("click", () => {
  const paragraphs = document.querySelectorAll("article p");
  paragraphs.forEach((p) => (p.style.fontWeight = "bold"));
});

// BONUS 1: Random font size on hover
h1.addEventListener("mouseover", () => {
  let randomSize = Math.floor(Math.random() * 100) + "px";
  h1.style.fontSize = randomSize;
});

// BONUS 2: Fade out 2nd paragraph on hover
const secondP = document.querySelectorAll("article p")[1];
secondP.style.transition = "opacity 1s";
secondP.addEventListener("mouseover", () => {
  secondP.style.opacity = "0";
});
secondP.addEventListener("mouseout", () => {
  secondP.style.opacity = "1";
});

// ===== Exercise 2

// 1. Retrieve the form
const form = document.querySelector("form");
console.log(form);

// 2. Retrieve inputs by id
const fnameInput = document.getElementById("fname");
const lnameInput = document.getElementById("lname");
console.log(fnameInput, lnameInput);

// 3. Retrieve inputs by name
const fnameByName = document.getElementsByName("firstname")[0];
const lnameByName = document.getElementsByName("lastname")[0];
console.log(fnameByName, lnameByName);

// 4. Handle form submit
form.addEventListener("submit", (e) => {
  e.preventDefault(); // prevent reload

  const fname = fnameInput.value.trim();
  const lname = lnameInput.value.trim();

  if (fname && lname) {
    const ul = document.querySelector(".usersAnswer");
    ul.innerHTML = ""; // clear previous values

    const li1 = document.createElement("li");
    li1.textContent = fname;
    ul.appendChild(li1);

    const li2 = document.createElement("li");
    li2.textContent = lname;
    ul.appendChild(li2);
  } else {
    alert("Please fill in both fields!");
  }
});

// ===== Exercise 3

let allBoldItems;

// Collect all bold items
function getBoldItems() {
  allBoldItems = document.querySelectorAll("p strong");
}
getBoldItems();

// Highlight bold text (blue)
function highlight() {
  allBoldItems.forEach((item) => (item.style.color = "blue"));
}

// Reset bold text (black)
function returnItemsToDefault() {
  allBoldItems.forEach((item) => (item.style.color = "black"));
}

// Apply on paragraph hover
const paragraph = document.querySelector("p");
paragraph.addEventListener("mouseover", highlight);
paragraph.addEventListener("mouseout", returnItemsToDefault);

// ===== Exercise 4

const formSphere = document.getElementById("MyForm");

formSphere.addEventListener("submit", (e) => {
  e.preventDefault();

  const radius = parseFloat(document.getElementById("radius").value);
  const volumeInput = document.getElementById("volume");

  if (!isNaN(radius)) {
    const volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
    volumeInput.value = volume.toFixed(2);
  } else {
    volumeInput.value = "Invalid input";
  }
});
