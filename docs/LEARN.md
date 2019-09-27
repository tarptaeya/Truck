# Truck Language Guide

### Declaring variable
```javascript
var x = 1
var y = x * x
var z = true and false
var w = "hello"
```

### Conditionals
**If Statement**
```javascript
if 4 > 2 {
    println("4 is greater than 2")
} else {
    println("2 is greater than 4")
}
```

**While Statement**
```javascript
var i = 0
while i <= 10 {
    println(i)
    i = i + 1
}
```

**Break and Continue**
```javascript
var i = 0
while true {
    if i >= 10 {
        break
    }
    i = i + 1
}
```

### Functions
**Function declaration**
```javascript
var sum = fn (x, y) {
    return x + y
}
```

### Comments
```javascript
/* C style comments are supported */
```

### Modules
Module declaration
```javascript
/* file: add.truck */
var add = fn(x, y) {
    return x + y
}
```
Importing module
```javascript
/* ...in some other file withing the same directory */
use "add"

var x = add(10, 20)
println(x) /* will print 30 */
```

### Built In Functions
**Print**
```javascript
print("Message") /* doesnt appends newline */
println("Hello World")
```

**Input**
```javascript
var x = input()
```

**Type**
```javascript
var x = "message"
type(x)
```

**Lenght**
```javascript
var x = "message"
len(x)
```

**Type converison**
```javascript
var x = num("24")
var y = "message " + str(32)
```

**Exit**
```javascript
exit(/*exit code*/0)
```
