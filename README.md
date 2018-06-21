Problem:
  Create a script that will take an input list, and create an output list that the elements are the product of 
  all the other elements of the list except the element at the corresponding index

Sample input
  [ 1, 3, 7, 5 ]

First element in output should be the product of all other elements except the first.
  first_element = 3*7*5  
  second_element = 1*7*5

Corresponding output list
  [105, 35, 15, 21]

Instead of looping thru and multiplying all elements except corresponding element:
  first pass multiply all elements
  second pass divide that product by the corresponding element

Product of all elements in sample input: 105
  first_element = 105 / 1
  second_element = 105 / 3  
