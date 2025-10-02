// ===== Exercise 1

<select id="genres">
  <option value="rock">Rock</option>
  <option value="blues" selected>
    Blues
  </option>
</select>;

{
  /* <script> */
}
// Get select element
const genres = document.getElementById("genres");

// Display selected value
console.log("Selected:", genres.value);

// Add new option
const classic = new Option("Classic", "classic", true, true);
// text = "Classic", value = "classic", defaultSelected = true, selected = true
genres.appendChild(classic);

console.log("Now selected:", genres.value);
// </script>

// ===== Exercise 2

{
  /* <form>
  <select id="colorSelect">
    <option>Red</option>
    <option>Green</option>
    <option>White</option>
    <option>Black</option>
  </select>
  <input type="button" value="Select and Remove">
</form> */
}

{
  /* <script> */
}
const button = document.querySelector("input[type=button]");
button.addEventListener("click", removecolor);

function removecolor() {
  const select = document.getElementById("colorSelect");
  select.remove(select.selectedIndex); // remove selected option
}
{
  /* </script> */
}

// ===== Exercise 3

let shoppingList = [];

// Get root
const root = document.getElementById("root");

// Create form
const form = document.createElement("form");
const input = document.createElement("input");
input.type = "text";
input.placeholder = "Enter item";
const addBtn = document.createElement("button");
addBtn.textContent = "Add Item";
addBtn.type = "submit";

// Append to form
form.appendChild(input);
form.appendChild(addBtn);

// Create UL for list
const ul = document.createElement("ul");

// Create ClearAll button
const clearBtn = document.createElement("button");
clearBtn.textContent = "Clear All";

// Add everything to DOM
root.appendChild(form);
root.appendChild(ul);
root.appendChild(clearBtn);

// Functions
form.addEventListener("submit", (e) => {
  e.preventDefault();
  addItem();
});

function addItem() {
  const value = input.value.trim();
  if (value === "") return;

  shoppingList.push(value);

  const li = document.createElement("li");
  li.textContent = value;
  ul.appendChild(li);

  input.value = ""; // clear input
}

clearBtn.addEventListener("click", clearAll);

function clearAll() {
  shoppingList = [];
  ul.innerHTML = ""; // clear DOM list
}
