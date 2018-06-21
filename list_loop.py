#!/usr/bin/env python3


input = [1,3,7,5]
expected_output = [105, 35, 15, 21]

output = []
total=1

#run thru list to get product of all items
for i in input:
  total=total*i

#loop thru list divide product by element
for i in range(len(input)):
  output.append(int(total/input[i]))

print("Input array:", input)
print("Expected output array:", expected_output)
print("Actual output array:  ", output)

if output == expected_output:
  print("Success")
else:
  print("Failure")
