import argparse
import sys

class Class1(object):
	def __init__(self):
		parser = argparse.ArgumentParser(description="Get parameters")
		group = parser.add_mutually_exclusive_group()
		group.add_argument("--param1", action="store_true", help="help of param1")
		group.add_argument("--param2", action="store_true", help="help of param2")
		group.add_argument("--param3", action="store_true", help="help of param3")
		group.add_argument("--param4", action="store_true", help="help of param4")
		group.add_argument("--param5", dest="command", action="store", choices=["cmd1","cmd2","cmd3"], help="help of param5")
		if len(sys.argv) > 1 and len(sys.argv) == 2:
			args = parser.parse_args(sys.argv[1:2])
		elif len(sys.argv) >= 3:
			args = parser.parse_args(sys.argv[1:3])
		else:
			parser.print_help()
			exit(1)

		if args.param1:
			param1func()
		elif args.param2:
			param2func()
		elif args.param3:
			param3func()
		elif args.param4:
			param4func()
		else:
			if len(sys.argv) == 2:
				parser.print_help()
				exit(1)
			else:
				if hasattr(self, args.command):
					getattr(self, args.command)()	
				else:
					parser.print_help()
					exit(1)

	def cmd1(self):
		cmd1func()

	def cmd2(self):
		cmd2func()

	def cmd3(self):
		parser = argparse.ArgumentParser(description="get or set",
			usage=str(sys.argv[0]) + " "
				+ str(sys.argv[1]) + " "
				+ str(sys.argv[2]) + " [-h] [--get | --set]")
		
		group = parser.add_mutually_exclusive_group()
		group.add_argument("--get", action="store_true", help="help of get")
		group.add_argument("--set", action="store_true", help="help of set")
		#parser.add_argument("--subcmd", dest="subcommand", choices=["get","set"], help="get or set")
		if len(sys.argv) < 4:
			parser.print_help()
			exit(1)
		args = parser.parse_args(sys.argv[3:5])
		if args.get:
			getfunc()
		elif args.set:
			setfunc()
		else:
			parser.print_help()
			exit(1)

def param1func():
	print("you choose parameter 1.")

def param2func():
	print("you choose parameter 2.")

def param3func():
	print("you choose parameter 3.")

def param4func():
	print("you choose parameter 4.")

def cmd1func():
	print("you choose parameter 5, cmd1.")

def cmd2func():
	print("you choose parameter 5, cmd2.")

def getfunc():
	print("you choose parameter 5, cmd3, get.")

def setfunc():
	print("you choose parameter 5, cmd3, set.")

#Main function
if __name__ == "__main__":
	Class1()