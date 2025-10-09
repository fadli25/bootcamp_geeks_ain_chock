// Exercise 1 :

class Bird {
  constructor() {
    console.log("I'm a bird. 🦢");
  }
}

class Flamingo extends Bird {
  constructor() {
    // This message runs first when we create a Flamingo.
    console.log("I'm pink. 🌸");
    // super() calls the parent class constructor (Bird).
    super();
  }
}

const pet = new Flamingo();

// 1. When 'new Flamingo()' is called:
//    → The Flamingo constructor starts executing.
//
// 2. The first console.log in Flamingo runs:
//    → Output: "I'm pink. 🌸"
//
// 3. Then 'super()' calls the Bird constructor.
//    → Output: "I'm a bird. 🦢"
//
// Final output (in order):
// I'm pink. 🌸
// I'm a bird. 🦢
