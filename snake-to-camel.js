function snakeToCamel(str) {
  // split the string and put the words into an array
  const arrFromStr = str.split('_');
  // create an array containing all but the first word of the array
  const arrNotFirst = arrFromStr.slice(1);

  // place the first word into a new array
  let newStrArr = [arrFromStr[0]];

  for (str of arrNotFirst) {
    str = capitalize(str);
    newStrArr.push(str);
  }
  newStr = newStrArr.join('');
  return newStr;
}

// Helper function that capitalizes a string
function capitalize(str) {
  strFirst = str[0].toUpperCase();
  strRest = str.substring(1);
  str = strFirst.concat(strRest);
  return str;
}

console.log("result1:", snakeToCamel("a_man_a_plan"));

