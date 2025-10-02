let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    paid: true,
    meansOfPayment: ["cash", "creditCard"],
  },
};

// 1. Display the fruits
const displayGroceries = () => {
  groceries.fruits.forEach((fruit) => console.log(fruit));
};

displayGroceries();
// Output: pear, apple, banana

// 2. Clone groceries and test pass by value/reference
const cloneGroceries = () => {
  // client is a primitive, copied by value
  let user = client;
  client = "Betty";
  console.log("user:", user);
  // Output: John, because primitives are copied by value

  // groceries is an object, copied by reference
  let shopping = groceries;

  shopping.totalPrice = "35$";
  shopping.other.paid = false;

  console.log("groceries.totalPrice:", groceries.totalPrice);
  // Output: 35$, changes affect the original object

  console.log("groceries.other.paid:", groceries.other.paid);
  // Output: false, changes affect the original object
};

cloneGroceries();
