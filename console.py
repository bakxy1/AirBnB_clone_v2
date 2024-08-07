#!/usr/bin/python3
"""Module defines a command line interpreter class"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """Interpreter class"""

    prompt = "(hbnb) " if sys.stdin.isatty() else ""

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Implement CTRL+D"""
        return True
    
    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()