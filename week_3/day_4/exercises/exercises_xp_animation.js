// ===== Exercise 1

// =========================
// Part I
// =========================
setTimeout(() => {
  alert("Hello World");
}, 2000);

// =========================
// Part II
// =========================
setTimeout(() => {
  const container = document.getElementById("container");
  const p = document.createElement("p");
  p.textContent = "Hello World";
  container.appendChild(p);
}, 2000);

// =========================
// Part III
// =========================
let counter = 0;
const container = document.getElementById("container");
const button = document.getElementById("clear");

let interval = setInterval(() => {
  const p = document.createElement("p");
  p.textContent = "Hello World";
  container.appendChild(p);
  counter++;

  // Stop when 5 paragraphs exist
  if (counter >= 5) {
    clearInterval(interval);
  }
}, 2000);

// Also stop manually if button clicked
button.addEventListener("click", () => {
  clearInterval(interval);
});

// ===== Exercise 2

function myMove() {
  const elem = document.getElementById("animate");
  let pos = 0;
  const containerWidth = document.getElementById("container").offsetWidth;
  const boxWidth = elem.offsetWidth;

  const id = setInterval(() => {
    if (pos >= containerWidth - boxWidth) {
      clearInterval(id);
    } else {
      pos++;
      elem.style.left = pos + "px";
    }
  }, 1); // move 1px every millisecond
}
