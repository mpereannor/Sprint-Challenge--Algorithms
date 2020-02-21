#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
a = 0  =>  assignment of a value to a, so we denote
a  notation of 1
0(1)

while (a < n * n * n ) => a while loop that will only stop at if a exceeds n** 3, 
0(n)

a = a + n * n  => assignment of a value to a, so we denote a notation of 1
0(1)

0(1) + 0(n) + 0(1)
runtime = 0(n)

b)
sum = 0 => assignment of a value 
0(1)

for i in range(n): => for loop taking in input of n
0(n)

j = 1 => assignment of a value 
0(1)

while j < n: => while loop that breaks with input value n
0(n)

j *=2  => assignment of a value 
0(1)

sum += 1 => assignment of a value 
0(1)

0(1) + 0(n) + 0(1) + 0(n) + 0(1) + 0(1)
0(3) + 0(2n)

runtime 0(n)

c)
if bunnies == 0  => assignment
0(1)
return 2 + bunnyEars(bunnies-1) => the function is being called recursively n times before reaching base case
O(n)
0(1) + 0(n)

runtime 0(n)


## Exercise II
1. Understand: 

algorithm that 
determines at what index in a list/floor an egg changes from whole to broken.

minimizes the number of dropped  and broken eggs 

what types of input can we expect 
 valid => int
 invalid => decimal, str, char

2. Plan 
first pass  - iterative approach

def chef_building (number of floors, eggs): 
  declare floor list 
  assign eggs at index[0] to f
  while floor is more than one:
    loop through floors:
     if 'eggs' at floor level is more than eggs at index[0]:
     assign floor level to f
      loop through floors again:
        if 'eggs' at floor level is more than eggs at f:
          assign floor level to min_destruction_level 
       
      loop once more:
        if 'eggs' at floor level is more than eggs at f: 
          assign floor level to min_destruction_level
  
  return min_destruction_level

  runtime complexity will be 0(n*2)



