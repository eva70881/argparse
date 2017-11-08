# argparse
This repository is a reference for python3 argparse

## Usage and result
    $ python main.py
Result shown as:
```
usage: main.py [-h]
               [--param1 | --param2 | --param3 | --param4 | --param5 {cmd1,cmd2,cmd3}]

Get parameters

optional arguments:
  -h, --help            show this help message and exit
  --param1              help of param1
  --param2              help of param2
  --param3              help of param3
  --param4              help of param4
  --param5 {cmd1,cmd2,cmd3}
                        help of param5
```
***
    $ python main.py --param1
Result shown as:
```
you choose parameter 1.
```
***
    $ python main.py --param2
Result shown as:
```
you choose parameter 2.
```
***
    $ python main.py --param3
Result shown as:
```
you choose parameter 3.
```
***
    $ python main.py --param4
Result shown as:
```
you choose parameter 4.
```
***
    $ python main.py --param5
Result shown as:
```
usage: main.py [-h]
               [--param1 | --param2 | --param3 | --param4 | --param5 {cmd1,cmd2,cmd3}]
main.py: error: argument --param5: expected one argument
```
***
    $ python main.py --param5 cmd1
Result shown as:
```
you choose parameter 5, cmd1.
```
***
    $ python main.py --param5 cmd2
Result shown as:
```
you choose parameter 5, cmd2.
```
***
    $ python main.py --param5 cmd3
Result shown as:
```
usage: main.py --param5 cmd3 [-h] [--get | --set]

get or set

optional arguments:
  -h, --help  show this help message and exit
  --get       help of get
  --set       help of set
```
***
    $ python main.py --param5 cmd3 --get
Result shown as:
```
you choose parameter 5, cmd3, get.
```
***
    $ python main.py --param5 cmd3 --set
Result shown as:
```
you choose parameter 5, cmd3, set.
```
