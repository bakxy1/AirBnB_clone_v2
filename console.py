#!/usr/bin/python3
"""Module defines a command line interpreter class"""
import cmd
import sys

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Interpreter class"""

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
    }

    prompt = "(hbnb) " if sys.stdin.isatty() else ""

    def default(self, line: str) -> None:
        arg: list = line.split(".")
        if arg[0] in HBNBCommand.__classes.keys() and arg[1] == "all()":
            all = storage.all()
            required_instances = [
                v for k, v in all.items() if k.split(".")[0] == arg[0]
            ]
            print("[", end="")
            for idx in range(len(required_instances)):
                print(required_instances[idx], end="")
                if idx + 1 != len(required_instances):
                    print(", ", end="")
            print("]")

        else:
            return super().default(line)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Implement CTRL+D"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates new instance of BaseModel"""
        arguments = line.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] in HBNBCommand.__classes.keys():
            obj = HBNBCommand.__classes.get(arguments[0])()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints string representation of an instance based on class name"""
        arguments = line.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            print(
                storage.all().get(f"{arguments[0]}.{arguments[1]}")
                or "** no instance found **"
            )

    def do_destroy(self, line):
        """Deletes an instance based on class name and ID"""
        arguments = line.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            if storage.all().get(f"{arguments[0]}.{arguments[1]}"):
                del storage.all()[f"{arguments[0]}.{arguments[1]}"]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all instances in string format"""
        arguments = line.split(" ")
        if arguments[0] == "":
            print([str(inst) for inst in storage.all().values()])
        elif arguments[0] in HBNBCommand.__classes.keys():
            print(
                [
                    str(storage.all()[key])
                    for key in storage.all().keys()
                    if key.split(".")[0] == arguments[0]
                ]
            )
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance"""
        arguments = line.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            instance = storage.all().get(f"{arguments[0]}.{arguments[1]}")

            if instance is not None:
                if len(arguments) == 2:
                    print("** attribute name missing **")
                elif len(arguments) == 3:
                    print("** value missing **")
                else:
                    setattr(instance, arguments[2], arguments[3])
                    storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
