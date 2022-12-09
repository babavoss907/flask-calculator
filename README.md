<!-- The challenge is to use Python, Flask, and Javascript to create a simple web-based
calculator such as the Mac or Windows calendars with the following features:

1. Create a flask page that displays a web calculator similar to the following layout
when the user visits the url http://127.0.0.1/calculator
The calculator can be rendered via an html table, or with a styled framework such
as bootstrap, or any other web-based method of your choosing.

2. When the user clicks numbers it will update the display of the calculator via
javascript so it functions like a typical calculator and will keep this value in
memory in a javascript variable (number variable).
3. When the user subsequently clicks a math operator such as + - x then the
following will happen:
a. Append the current number variable to a javascript array.
b. Append the operation clicked to the javascript array.
c. if the user then clicks a number it will reset the display and   go to step 2 like a typical calculator.
4. When the user clicks the = sign it will use AJAX to send the javascript array that
contains all the previously clicked numbers and operators to a Flask endpoint for
processing.
5. The Flask endpoint will take the array of numbers and operators and perform a
math operation on the array such as 3 + 5 - 9 and return the result as the
response to the AJAX call.
6. The calculator page will get the response from the AJAX call and update the
display of the calculator to hold the resulting value.
7. Return to step 2 so the user may continue using the calculator. -->
# Flask Calculator

1. "pip install requirements.txt"

2. in terminal "flask run"