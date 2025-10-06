#************************************************************
#   Module:             backend.datamodule.config (PocketA) *
#   Author:             Scavenger4208                       *
#   Version:            0.0.1                               *
#************************************************************

#=== Imports

import os
from dotenv import load_dotenv

# load file .env
load_dotenv()

#=== defs and classes

def config_db():
    # db dict
    db = {}

    # Call variables and add to dict db
    db['host'] = os.getenv("DB_HOST")
    db['port'] = os.getenv("DB_PORT")
    db['dbname'] = os.getenv("DB_NAME")
    db['user'] = os.getenv("DB_USER")
    db['password'] = os.getenv("DB_PASSWORD")

    return db
