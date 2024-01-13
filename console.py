#!/usr/bin/python3
"""This Module defines one class: HBNBCommand
"""

import sys
import re
import cmd
import os
from models.__init__ import storage
import models.interface


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""
    use_rawinput = os.isatty(sys.stdout.fileno())

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def precmd(self, line):
        """overrides parent precmd method"""
        pattern = (r'^(..{0,})\.([a-z]{1}[a-zA-Z0-9_]*)'
                   r'\(([a-zA-Z0-9,_\-\s\{\}:"\']*)\)$')
        line = line.strip()
        result = re.search(pattern, line)
        if result:
            cls_name = result.group(1)
            method = result.group(2)
            arg = result.group(3)
            command = method + ' ' + cls_name + ' '
            if arg != '':
                args = self.__parseArgs(arg, ',')
                command += ' '.join(args)
            return command
        else:
            return super().precmd(line)

    def do_clear(self, arg):
        """clear terminal screen"""
        from os import system, name
        if name == 'nt':
            system('cls')
        else:
            system('clear')

    def help_clear(self):
        """print help for cleare command"""
        print("Usage:")
        print("========")
        print("clear\n")
        print("Description:")
        print("============")
        print("clear the terminal screen\n")
        print("Examples:")
        print("===========")
        print("clear\n")

    def do_count(self, arg):
        """print  the number of instances of a class"""
        if not arg:
            print("** class name missing **")
        elif not hasattr(models.interface, arg):
            print("** class doesn't exist **")
        else:
            objs = storage.findByClassName(arg)
            print(len(objs))

    def help_count(self):
        """print help for count command"""
        print("Usage:")
        print("==============")
        print("\tcount <class name>")
        print("\t<class name>.count()\n")
        print("Description:")
        print("==============")
        print("\tretrieve the number of instances of a class\n")
        print("Examples:")
        print("==============")
        print("\tcount BaseModel")
        print("\tUser.count()\n")

    def do_quit(self, args):
        """quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, args):
        """press CTRL+D to quit"""
        print()
        return True

    def help_quit(self):
        """help on quit command"""
        print("\t quit - exit command line\n")
        print("Usage:")
        print("=========")
        print("\tquit")
        print("Description:")
        print("=============")
        print("\tQuit command to exit the program\n")

    def help_EOF(self):
        """help on EOF command"""
        print("press CTRL+D on linux to quit!")

    def emptyline(self):
        """get executed when press Enter without entering anything"""
        return False

    def do_create(self, arg):
        """create instance of class"""
        if not arg:
            print("** class name missing **")
        elif not hasattr(models.interface, arg):
            print("** class doesn't exist **")
        else:
            cls = getattr(models.interface, arg)
            obj = cls()
            obj.save()
            print(obj.id)

    def help_create(self):
        """print help for create command"""
        print("Usage:")
        print("=============")
        print("\tcreate class_name")
        print("\tclass_name.create()\n")
        print("Description:")
        print("=============")
        print(("\tCreates a new instance of class: "
               "class_name and add to file.json"))
        print("\tthen print the id of newly created instance if successful\n")
        print("Examples:")
        print("=============")
        print("\tcreate BaseModel")
        print("\tUser.create()\n")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = self.__parseArgs(arg)
        obj_id = None if len(args) < 2 or args[1] == '' else args[1].strip('"')
        cls_name = None if len(args) <= 0 else args[0].strip('"')
        if not cls_name:
            print("** class name missing **")
        elif not hasattr(models.interface, cls_name):
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        else:
            obj = storage.find(cls_name, obj_id)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def help_show(self):
        """Prints help of show command"""
        print("Usage:\n")
        print("\tshow <class name> <id>")
        print("\t<class name>.show(<id>)\n")
        print("Description:\n")
        print(("\tPrints the string representation of an"
               " instance based on the class name and id"))
        print("Examples:\n")
        print("\tshow BaseModel 123-123-123")
        print("\tBaseModel.show(123-123)\n")

    def __parseArgs(self, arg, sep=None):
        """parse command arguments and return a list of args"""
        def isseparator(arg, sep):
            return arg.isspace() if sep is None else arg == sep
        args = []
        if not arg:
            return args
        start = 0
        current = 0
        length = len(arg)
        while current < length:
            if isseparator(arg[current], sep):
                current += 1
                while current < length and arg[current].isspace():
                    current += 1
            elif arg[current] == '"':
                idx = arg.find('"', current + 1)
                if idx != -1:
                    args.append(arg[current:idx + 1])
                    current = idx + 1
                else:
                    args.append(arg[current:])
                    current = length
            elif arg[current] == '{':
                idx = arg.find('}', current)
                if idx != -1:
                    val = arg[current: idx + 1]
                    current = idx + 1
                else:
                    val = arg[current:]
                    current = length
                args.append(val)
            else:
                while (current < length and not isseparator(arg[current], sep)
                        and arg[current] != '"'):
                    current += 1
                args.append(arg[start: current])
            start = current
        return args

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = self.__parseArgs(arg)
        cls_name = None if len(args) <= 0 else args[0]
        obj_id = None if len(args) < 2 or args[1] == '' else args[1].strip('"')
        if not cls_name:
            print("** class name missing **")
        elif not hasattr(models.interface, cls_name):
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        elif not storage.destroy(cls_name, obj_id):
            print("** no instance found **")

    def help_destroy(self):
        """Prints destroy command help"""
        print("Usage:")
        print("===========")
        print("\tdestroy <class name> <id>")
        print("\t<class name>.destroy(<id>)\n")
        print("Description:")
        print("============")
        print(("\tDeletes an instance based on the class "
               "name and id (save the change into the JSON file\n"))
        print("Examples:")
        print("============")
        print("\tdestroy BaseModel 49faff9a-6318-451f-87b6-910505c55907")
        print('\tBaseModel.destroy("49faff9a-6318-451f-87b6-910505c55907")\n')

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        if not arg:
            print(storage.findAll())
        elif not hasattr(models.interface, arg):
            print("** class doesn't exist **")
        else:
            print(storage.findByClassName(arg))

    def help_all(self):
        """Prints all command help"""
        print("Usage:")
        print("=============")
        print("\tall [class name]")
        print("\t<class name>.all()\n")
        print("Description:")
        print("==============")
        print(("\tPrints all string representation of "
               "all instances based or not on the class name.\n"))
        print("Examples:")
        print("==============")
        print("\tall -> print all classes")
        print("\tall User -> print all class User instances")
        print("\tBaseModel.all()\n")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        from ast import literal_eval
        args = self.__parseArgs(arg)
        length = len(args)
        cls_name = None if length == 0 else args[0].strip('"')
        obj_id = None if length < 2 or args[1] == '' else args[1].strip('"')
        if not cls_name:
            print("** class name missing **")
        elif not hasattr(models.interface, cls_name):
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        else:
            obj = storage.find(cls_name, obj_id)
            if obj:
                attribute_name = None if length < 3 else args[2].strip('"')
                attribute_value = None if length < 4 else args[3].strip('"')
                if not attribute_name:
                    print("** attribute name missing **")
                elif not attribute_value:
                    print("** value missing **")
                else:
                    kw = {attribute_name: attribute_value}
                    obj.addOrUpdate(**kw)
                    obj.save()
            else:
                print("** no instance found **")

    def help_update(self):
        """Prints update command help text"""
        print(('\tupdate -  Updates an instance based '
               'on the class name and id\n'))
        print('Usage:\n')
        print(('\tupdate <class name> <id> <attribute name> '
               '"<attribute value>"'))
        print(('\t<class_name>.update(<id>, <attribute name>, '
               '"<attribute value>")'))
        print('\t<class name>.update(<id>, <dictionary representation>)')
        print('Description:\n')
        print("\tUpdates an instance based on the class name and id")
        print(("\tby adding or updating attribute "
               "(save the change into the JSON file)\n"))
        print('Examples:\n')
        print('\tupdate BaseModel 1234-1234-1234 email "aibnb@mail.com"')
        print('\tupdate BaseModel 1234-1234 {\'first_name\': "Jhon"}')
        print(('\tUser.update("38f22813-2753-4d42-b37c-57a17f1e4f88", '
               '"first_name", "John")'))
        print(('\tUser.update("38f22813-2753-4d42-b37c-57a17f1e4f88",'
               ' "age", 89)'))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
