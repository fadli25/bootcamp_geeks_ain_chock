// 1

let sentence = "This movie is not that bad !";

// 2
let wordNot = sentence.indexOf("not");

// 3
let wordBad = sentence.indexOf("bad");

// 4
if (wordNot == -1 || wordNot > wordBad) {
  console.log(sentence);
} else {
  console.log(
    sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad + 3)
  );
}
