#!/usr/bin/python3

""" DATABASE and FILE STORAGE SWITCH """
from os import getenv

storage_switch = getenv('HBNB_TYPE_STORAGE')
if storage_switch == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
