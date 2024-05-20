#!/usr/bin/python3
"""Console module - entry point of the command interpreter"""
import cmd
import json
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    # --- Advanced tasks ---
    def dict_update(self, classname, uid, s_dict):
        """updates an instance from a dictionary"""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def adv_parser(self, arg):
        """Rearranges commands of syntax class.< command >()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not match:
            return arg
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def default(self, arg):
        """Redirects input to adv_parser when syntax doesn't match"""
        response = self.adv_parser(arg)
        if response == arg:
            print("*** Unknown syntax:", arg)

    def do_count(self, arg):
        """Retrieves the number of instances of a class
        Usage: <class name>.count()"""
        objs = storage.all()
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes_dict():
            print("** class doesn't exist **")
        else:
            instances = 0
            for id in objs.keys():
                classs = id.split(".")
                if arg == classs[0]:
                    instances += 1
            print(instances)

    # --- More functionality (console 0.1.0) ---
    def do_create(self, arg):
        """Creates a new instance of a class"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes_dict():
            print("** class doesn't exist **")
        else:
            base1 = storage.classes_dict()[arg]()
            base1.save()
            print(base1.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        objs = storage.all()
        args = self.parse(arg)
        if args is None:
            return
        for id in objs.keys():
            if id == args[0] + "." + args[1]:
                print(objs[id])
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        objs = storage.all()
        args = self.parse(arg)
        if args is None:
            return
        for id in objs.keys():
            if id == args[0] + "." + args[1]:
                del objs[id]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        objs = storage.all()
        args = self.parse(arg)
        if args is None:
            return
        s_pttn = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|\
                 (?:(\S)+)))?)?)?'
        m = re.search(s_pttn, arg)
        classname = m.group(1)
        uid = m.group(2)
        attribute = m.group(3)
        value = m.group(4)
        if not m:
            print("** class name missing **")
        elif classname not in storage.classes_dict():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attr_dict()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = storage.all()
        objs_list = []
        if arg != "" and arg is not None:
            args = arg.split()
            if args[0] not in storage.classes_dict():
                print("** class doesn't exist **")
            else:
                for id in objs.keys():
                    if objs[id].__class__.__name__ == args[0]:
                        objs_list.append(objs[id].__str__())
        else:
            for id in objs.keys():
                objs_list.append(objs[id].__str__())
        if len(objs_list) > 0:
            print(objs_list)

    # --- Basic functionality (console 0.0.1) ---
    def do_EOF(self, *arg):
        """Exits program at EOF"""
        print()
        return True

    def do_quit(self, *arg):
        """QUIT command that exits the program"""
        return True

    def emptyline(self):
        """Does nothing on an empty line + ENTER"""
        pass

    def parse(self, arg):
        """helper method for parsing string input"""
        if arg == "" or arg is None:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if args[0] not in storage.classes_dict():
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id is missing **")
                return
            return args


if __name__ == "__main__":
    HBNBCommand().cmdloop()
