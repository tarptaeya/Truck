Truck is a dynamic programming language with a focus on simplicity.

### Example
```truck
use io

class Greeter {
  constructor(name) {
    this.name = name
  }

  salute() {
    print("Hello " + this.name)
  }
}

g = Greeter("world")
g.salute()
```

### Getting started
```bash
git clone http://github.com/tarptaeya/truck
cd truck
python3 -m truck #[filename] or leave empty to run repl
```

### Syntax highlighting
Syntax highlighting for vim is supported and associated files can be found in the vim directory of the project. Either copy the files yourself or execute `install_vim.sh` to automatically copy the vim files for you.
