![Truck Banner](https://github.com/Tarptaeya/Truck/blob/master/banner.png)


Truck is a dynamic toy programming language with a focus on simplicity

Truck interpreter is implemented as a tree walking interpreter with **hand written recursive descent parser** in Python without any external dependency.

### Example
Program to print nth fibonacci number
```javascript
var fibonacci = fn(x) {
    if x <= 1 {
        return 1
    }

    return fibonacci(x - 1) + fibonacci(x - 2)
}

var n = num(input())
print(fibonacci(n))
```
More examples can be found at [/examples](https://github.com/Tarptaeya/Truck/tree/master/examples).

### Getting started
```bash
git clone http://github.com/tarptaeya/truck
cd truck
python3 truck/truck.py #[filename] or leave empty to run repl
```

### Learn
Checkout [LEARN.md](https://github.com/Tarptaeya/Truck/tree/master/docs/LEARN.md) to learn programming in truck.

### Syntax highlighting
Syntax highlighting for vim is supported and associated files can be found in the vim directory of the project. Either copy the files yourself or execute `install_vim.sh` to automatically copy the vim files for you.
