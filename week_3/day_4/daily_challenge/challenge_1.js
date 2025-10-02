const form = document.getElementById("libform");
const storySpan = document.getElementById("story");

// Add a shuffle button
const shuffleBtn = document.createElement("button");
shuffleBtn.textContent = "Shuffle Story";
shuffleBtn.type = "button";
form.appendChild(shuffleBtn);

let currentValues = {};
let stories = [];
let usedStories = [];

// Event when form is submitted
form.addEventListener("submit", function (e) {
  e.preventDefault();

  // Get values
  const noun = document.getElementById("noun").value.trim();
  const adj = document.getElementById("adjective").value.trim();
  const person = document.getElementById("person").value.trim();
  const verb = document.getElementById("verb").value.trim();
  const place = document.getElementById("place").value.trim();

  // Validation
  if (!noun || !adj || !person || !verb || !place) {
    alert("Please fill in all fields!");
    return;
  }

  // Save current values for shuffle use
  currentValues = { noun, adj, person, verb, place };

  // Possible stories
  stories = [
    `${person} decided to ${verb} with a ${adj} ${noun} in ${place}.`,
    `In ${place}, ${person} found a ${adj} ${noun} and tried to ${verb} it.`,
    `A ${adj} ${noun} wanted to ${verb}, so ${person} helped in ${place}.`,
  ];

  // Reset used stories so shuffle can start fresh
  usedStories = [];

  // Display first story
  displayStory();
});

// Display a story (random but not repeated until all are used)
function displayStory() {
  if (usedStories.length === stories.length) {
    usedStories = []; // reset if all used
  }

  let remaining = stories.filter((s) => !usedStories.includes(s));
  let randomStory = remaining[Math.floor(Math.random() * remaining.length)];

  storySpan.textContent = randomStory;
  usedStories.push(randomStory);
}

// Shuffle button event
shuffleBtn.addEventListener("click", function () {
  if (Object.keys(currentValues).length === 0) {
    alert("Fill in the form first!");
    return;
  }
  displayStory();
});
