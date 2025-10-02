const mergeWords = (word) => {
  let sentence = word || "";

  const inner = (nextWord) => {
    if (nextWord === undefined) {
      return sentence;
    }
    sentence += " " + nextWord;
    return inner;
  };

  return inner;
};

// Examples
console.log(mergeWords("Hello")()); // "Hello"
console.log(mergeWords("There")("is")("no")("spoon.")()); // "There is no spoon."
