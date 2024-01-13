#!/usr/bin/python3
"""init models module"""


from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
