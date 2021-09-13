# -*- coding: utf-8 -*-

import os, sys
import sqlite3

from core.data import *

# Create a Database with sqlite3 if there is no database.
if not os.path.isfile('data/database.db'):
    create_DB()
else:
    print("Database already exists!")
