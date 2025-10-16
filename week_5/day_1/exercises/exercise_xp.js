// Exercise 1

function compareToTen(num) {
  return new Promise((resolve, reject) => {
    if (num <= 10) {
      resolve(`${num} is less or equal to 10`);
    } else {
      reject(`${num} is greater than 10`);
    }
  });
}

// Exercise 2

const promise = new Promise((resolve) => {
  setTimeout(() => {
    resolve("success");
  }, 4000);
});

promise.then((result) => console.log(result));

// Exercise 3

// 1.

const p = Promise.resolve(3);

// 2.

const d = Promise.reject("Boo!");
