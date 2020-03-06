# Packaging Python Into CLI Commands

### Install
```
python setup.py install
```

### Now You Have A CLI Command!
```
key word is "fudo" for this package

fudo --verbose
fudo --sushi
fudo --spell
```

### How It Works
```
- package is built
- arge parser calls the appropriate function
- see setup.py to see how to set commands
* Packages are named poorly for simplicity
```