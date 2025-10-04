function areAnagrams(str1, str2) {
  // Helper function: normalize string by removing spaces and lowercasing
  const normalize = (str) =>
    str.replace(/\s+/g, "").toLowerCase().split("").sort().join("");
  return normalize(str1) === normalize(str2);
}

// Examples
console.log(areAnagrams("Astronomer", "Moon starer")); // true
console.log(areAnagrams("School master", "The classroom")); // true
console.log(areAnagrams("The Morse Code", "Here come dots")); // true
console.log(areAnagrams("Hello", "Olelh")); // true
console.log(areAnagrams("Hello", "World")); // false
