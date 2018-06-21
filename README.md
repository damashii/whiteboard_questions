Problem:\
&nbsp;&nbsp;Create a script that will take an input list, and create an output list that the elements are the product of all the other elements of the list except the element at the corresponding index

Sample input:\
&nbsp;&nbsp;[ 1, 3, 7, 5 ]

First element in output should be the product of all other elements except the first.\
&nbsp;&nbsp;first_element = 3 * 7 * 5\
&nbsp;&nbsp;second_element = 1 * 7 * 5

Corresponding output list:\
&nbsp;&nbsp;[105, 35, 15, 21]

Instead of looping thru and multiplying all elements except corresponding element:\
&nbsp;&nbsp;first pass multiply all elements\
&nbsp;&nbsp;second pass divide that product by the corresponding element\

Product of all elements in sample input: 105\
&nbsp;&nbsp;first_element = 105 / 1\
&nbsp;&nbsp;second_element = 105 / 3

