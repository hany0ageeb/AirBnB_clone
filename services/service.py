#!/usr/bin/python3


import models.interface


class InvalidClassNameError(Exception):
    def __init__(self, class_name, message="** class doesn't exist **"):
        self.class_name = class_name
        super().__init__(message)


class MissingInstanceIdError(Exception):
    def __init__(self, message="** instance id missing **"):
        super().__init__(message)


class Service:

    __missing_msg = "** class name missing **"

    def create(self, cls_name):
        if not cls_name:
            raise InvalidClassNameError(cls_name, Service.__missing_msg)
        if not hasattr(models.interface, cls_name):
            raise InvalidClassNameError(cls_name)
        cls = getattr(models.interface, cls_name)
        obj = cls()
        obj.save()
        return obj

    def count(self, cls_name):
        from models import storage
        if not cls_name:
            raise InvalidClassNameError(cls_name, Service.__missing_msg)
        if not hasattr(models.interface, cls_name):
            raise InvalidClassNameError(cls_name)
        count = 0
        objs = storage.findByClassName(cls_name)
        count = len(objs)
        return count

    def show(self, cls_name, obj_id):
        from models import storage
        if not cls_name:
            raise InvalidClassNameError(cls_name, Service.__missing_msg)
        if not hasattr(models.interface, cls_name):
            raise InvalidClassNameError(cls_name)
        if obj_id:
            return storage.find(cls_name, obj_id)
        else:
            raise MissingInstanceIdError()

    def destroy(self, cls_name, obj_id):
        from models import storage
        if not cls_name:
            raise InvalidClassNameError(cls_name, Service.__missing_msg)
        if not hasattr(models.interface, cls_name):
            raise InvalidClassNameError(cls_name)
        if obj_id:
            return storage.destroy(cls_name, obj_id)
        else:
            raise MissingInstanceIdError()

    def all(self, cls_name):
        from models import storage
        if cls_name:
            if not hasattr(models.interface, cls_name):
                raise InvalidClassNameError(cls_name)
            return storage.findByClassName(cls_name)
        return storage.findAll()

    def update(self, cls_name, obj_id, **kwargs):
        if not cls_name:
            raise InvalidClassNameError(cls_name, Service.__missing_msg)
        if not hasattr(models.interface, cls_name):
            raise InvalidClassNameError(cls_name)
        if not obj_id:
            raise MissingInstanceIdError()
        instance = None
        if kwargs is not None:
            from models import storage
            instance = storage.find(cls_name, obj_id)
            if instance is not None:
                instance.addOrUpdate(**kwargs)
                instance.save()
        return instance
