# -*- coding: utf-8 -*-

import os, sys, socket
import sqlite3

from core.data import *

# Create a Database with sqlite3 if there is no database.
db = DB("data.db")



main_menu = """
    1. Add an item              4. Create an item
    2. Remove an item           5. Delete an item
    3. Get an item              6. See all items
"""

# USER INPUT
try:
    while True:
        ui = input(str(f"$ {socket.gethostname()} "))
        if ui == "1":
            print("Add an item")
        elif ui == "2":
            pass
        elif ui == "3":
            pass
        elif ui == "4":
            pass
        elif ui == "5":
            pass
        elif ui == "6":
            pass
        else:
            continue

except KeyboardInterrupt:
    sys.exit(0)
