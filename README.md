![Argonaut-Lang](https://user-images.githubusercontent.com/86574651/123707032-17430080-d837-11eb-99e0-355b9557a73a.png)
# Argonaut-Lang
The Argonaut Programming Language


Argonaut is my first programming language, made with the [ply](https://github.com/dabeaz/ply) python library. Since it's my first language, it's *very* bad and should not be used for anything other than play. 🤣 It has no scoping and terrible error catching. Enjoy!

>(You must install the [ply](https://github.com/dabeaz/ply) python library before you can use Argonaut!)

## Here's the documentation anyway:
<br>

### Comments:
```
[- comment -]

[- Comments
are always
multi-line -]
```
### I/O:
```
log(...);
input(...);
```
### Variables:
```
var -> 12;
log(var);
```
### Math:
```js
5 + 2 = 7
5 - 2 = 3
5 * 2 = 10
5 / 2 = 2.5
5 ^ 2 = 25
5 % 2 = 1
```
### Conditions:
```js
5 == 2 : false
5 != 2 : true
5 > 2  : true
5 < 2  : false

and or not
```
### If / OWise:
```
if (condition) {
  ...
}
	
if (condition) {
  ...
} owise {
  ...
}
```
### Loops:
```
loop (expression) {
  ...
}
```
### Creating/Calling Functions:
Super basic, no arguments.
```
fun (funcName) (returnExpr) {
  
}

(fun);
```
### Built-in functions:
There are basically none:
```
log(...); [- Already covered -]
input(...); [- Already covered -]
toInt(...); [- Converts the argument to an integer value -]
```

## Examples

Simple greeting program:
```
name -> input("What is your name? ");
log("Hello, " + name + "!");

[- Output:
What is your name? MystPi
Hello, MystPi!
-]
```

Basic functions:
```
fun (add) (a + b) {
  log("Adding numbers..");
}

a -> 1;
b -> 2;
log((add));

[- Output:
Adding numbers..
3
-]
```

## How to run code:
Add this to a python file:
```python
from argonautParser import runCode
runCode(your code here)
```

## Other notes
Please add an issue if you find any errors in the source code or this README. Thanks! 🙏
