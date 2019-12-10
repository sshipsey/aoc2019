const part1 = (min: number, max: number) => {
  let ans = 0;
  let double = false;
  let increment = true;

  for (let i = min; i <= max; i++) {
    for (let j = 0; j < i.toString().length - 1; j++) {
      if (i.toString()[j] === i.toString()[j + 1]) {
        double = true;
      }
      if (!(Number(i.toString()[j]) <= Number(i.toString()[j + 1]))) {
        increment = false;
      }
    }

    if (double && increment) {
      ans += 1;
    }
    double = false;
    increment = true;
  }
  return ans;
};

const part2 = (min: number, max: number) => {
  let ans = 0;
  let double = false;
  let increment = true;
  let groupSize = 0;
  for (let i = min; i <= max; i++) {
    for (let j = 0; j < i.toString().length - 1; j++) {}
  }
};

const min = 347312;
const max = 805915;

console.log(part1(min, max));
console.log(part2(min, max));
