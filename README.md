# Flask Calculator

##### A simple web-based calculator similar to the Mac or Windows calulator with the following features:

1. When the user clicks numbers it will update the display of the calculator via
javascript so it functions like a typical calculator and will keep this value in
memory in a javascript variable (number variable).
2. When the user subsequently clicks a math operator such as + - x then the
following will happen:
- Append the current number variable to a javascript array.
- Append the operation clicked to the javascript array.
- if the user then clicks a number it will reset the display and   go to step 2 like a typical calculator.
3. When the user clicks the = sign it will use AJAX to send the javascript array that
contains all the previously clicked numbers and operators to a Flask endpoint for
processing.
4. The Flask endpoint will take the array of numbers and operators and perform a
math operation on the array such as 3 + 5 - 9 and return the result as the
response to the AJAX call.
5. The calculator page will get the response from the AJAX call and update the
display of the calculator to hold the resulting value.
6. Return to step 2 so the user may continue using the calculator.

###### An IOS Calculator replica using Flask

## Prerequisites

- Python 3.9.0 (64 bit)
- Pip >= 20.2.x

###### 1. Installing Python 3.9.X if not installed already

###### Steps for Linux Users

- Follow the below steps to install python 3.9.6 version

```
$ wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
$ tar -xzf Python-3.9.6.tgz
$ cd Python-3.9.6/
$ ./configure --enable-optimizations
$ make altinstall
```

###### Steps for Windows Users

- Please download Windows installer - https://www.python.org/downloads/release/python-396/
- You can follow the installation steps by clicking on the executable
- You can choose the python install directory during this installation

###### 2. Installing pipenv

```
$ pip install pipenv
```

###### 3. Cloning repository

```
$ git clone https://github.com/babavoss907/flask-calculator.git
```

###### 4. Change directory

```
$ cd flask-calculator
```

###### 5. Create shell

```
$ pipenv shell
```

###### 6. Install dependencies

```
$ pip install requirements.txt
```

###### 7. Run app

```
$ flask run
```

###### 8. Go to local host to view calculator

http://127.0.0.1:5000/calculator