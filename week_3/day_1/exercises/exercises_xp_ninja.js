// ===== Exercise 1

const person1 = {
  fullName: "Alice Smith",
  mass: 68, // in kg
  height: 1.65, // in meters
  calcBMI: function () {
    return this.mass / (this.height * this.height);
  },
};

const person2 = {
  fullName: "Bob Johnson",
  mass: 85, // in kg
  height: 1.8, // in meters
  calcBMI: function () {
    return this.mass / (this.height * this.height);
  },
};

function compareBMI(p1, p2) {
  const bmi1 = p1.calcBMI();
  const bmi2 = p2.calcBMI();
  if (bmi1 > bmi2) {
    console.log(`${p1.fullName} has the largest BMI (${bmi1.toFixed(2)})`);
  } else if (bmi2 > bmi1) {
    console.log(`${p2.fullName} has the largest BMI (${bmi2.toFixed(2)})`);
  } else {
    console.log(`Both have the same BMI (${bmi1.toFixed(2)})`);
  }
}

compareBMI(person1, person2);

// ===== Exercise 2

function calculateAverage(gradesList) {
  const sum = gradesList.reduce((acc, grade) => acc + grade, 0);
  return sum / gradesList.length;
}

function findAvg(gradesList) {
  const average = calculateAverage(gradesList);
  console.log(`Average grade: ${average.toFixed(2)}`);
  if (average > 65) {
    console.log("Congratulations, you passed!");
  } else {
    console.log("You failed and must repeat the course.");
  }
}

// Example usage:
findAvg([70, 80, 90, 60, 50]);
