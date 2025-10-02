// Exercise 1 : Analyzing the map method
const result1 = [1, 2, 3].map((num) => {
  if (typeof num === "number") return num * 2;
  return; // implicitly returns undefined if condition fails
});
console.log(result1);
// Output: [2, 4, 6]
// Explanation: Each element is a number, so num*2 is returned for each.

// Exercise 2 : Analyzing the reduce method
const result2 = [
  [0, 1],
  [2, 3],
].reduce(
  (acc, cur) => {
    return acc.concat(cur);
  },
  [1, 2]
);
console.log(result2);
// Output: [1, 2, 0, 1, 2, 3]
// Explanation: The initial value of acc is [1,2], then each sub-array is concatenated.

//  Exercise 3 : Analyze this code
const arrayNum = [1, 2, 4, 5, 8, 9];
const newArray = arrayNum.map((num, i) => {
  console.log(num, i); // logs element and its index
  alert(num); // shows element in alert
  return num * 2;
});
console.log(newArray);
// Value of i: the index of the current element in arrayNum (0,1,2,3,...)

// Exercise 4 : Nested arrays

// 1. Flatten [[1],[2],[3],[[[4]]],[[[5]]]] into [1,2,3,[4],[5]]
const array = [[1], [2], [3], [[[4]]], [[[5]]]];
const flattened = array.map((el) => el.flat(2));
console.log(flattened);
// Output: [1,2,3,[4],[5]]

// 2. Flatten greeting array into joined strings
const greeting = [
  ["Hello", "young", "grasshopper!"],
  ["you", "are"],
  ["learning", "fast!"],
];
const greetingFlattened = greeting.map((subArr) => subArr.join(" "));
console.log(greetingFlattened);
// Output: ["Hello young grasshopper!","you are","learning fast!"]

// 3. Turn greetingFlattened into a single string
const greetingString = greetingFlattened.join(" ");
console.log(greetingString);
// Output: "Hello young grasshopper! you are learning fast!"

// 4. Turn trapped number into [3]
const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]];
const trappedFlattened = trapped.flat(Infinity);
console.log(trappedFlattened);
// Output: [3]
