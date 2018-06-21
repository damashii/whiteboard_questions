#!/usr/bin/env python3

def arry(input):
  output = []
  total=1

  #run thru list to get product of all items
  for i in input:
    total=total*i

  #if an element is 0 total will be 0, will cause a divide by zero error in next step
  if total == 0:
    output = [0]*len(input)
  else:
  #loop thru list divide product by element
    for i in range(len(input)):
      output.append(int(total/input[i]))

  return output


def test_me(gazin, expected_output):
  gazout = arry(gazin)
  
  print("Input array:", gazin)
  print("Expected output array:", expected_output)
  print("Actual output array:  ", gazout)

  if gazout == expected_output:
    print("Success")
  else:
    print("Failure")

initial_in = [1,3,7,5]
initial_output = [105, 35, 15, 21]

test_me(initial_in, initial_output)

break_me = [1,3,7,5,0]
break_out = [0,0,0,0,0]

test_me(break_me, break_out)

