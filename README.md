[![Build Status](https://travis-ci.org/Tarptaeya/Truck.svg?branch=master)](https://travis-ci.org/Tarptaeya/Truck) [![Build status](https://ci.appveyor.com/api/projects/status/ovgiyt7fldy7fujb/branch/master?svg=true)](https://ci.appveyor.com/project/Tarptaeya/truck/branch/master)

Truck is a dynamic programming language with a focus on simplicity.

### Example
```truck
use io

class Greeter {
  constructor(name) {
    this.name = name
  }

  salute() {
    io.println("Hello " + this.name)
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
