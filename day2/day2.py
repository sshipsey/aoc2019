import copy

def part1(input):
  ptr = 0
  while (ptr < len(input) - 4 and input[ptr] != 99):
    if (input[ptr] == 1):
      input[input[ptr + 3]] = input[input[ptr + 1]] + input[input[ptr + 2]]
      ptr += 4
      continue
    elif (input[ptr] == 2):
      input[input[ptr + 3]] = input[input[ptr + 1]] * input[input[ptr + 2]]
      ptr += 4
      continue
  return input[0]

def part2(input):
  target = 19690720
  noun = 0
  verb = 0
  while (verb < 99):
    # reset computer
    _input = copy.copy(input)
    _input[1] = noun
    _input[2] = verb

    #test
    if(part1(_input) == target):
      return 100 * noun + verb
 
    # update inputs
    noun += 1
    if (noun > 99):
      noun = 0
      verb += 1

  return "failure"



input1 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
input2 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]

print(part1(input1))
print(part2(input2))