#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:06:48 2020
@author: hantswilliams
"""

import os
from dotenv import load_dotenv
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


### PLEASE USE .ENV FILE TO STORE YOUR PASSWORDS, USERNAMES, HOSTNAME, ETC. ###

MYSQL_HOSTNAME = 'inserthere'
MYSQL_USER = 'inserthere'
MYSQL_PASSWORD = 'inserthere'
MYSQL_DATABASE = 'ahi'

# Correct way example here:  https://pypi.org/project/python-dotenv/
# use dotenv to load in environment variables
load_dotenv()
MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


########

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3305/{MYSQL_DATABASE}'
engine = create_engine(connection_string)


TABLENAME = MYSQL_USER + 'patient_portal'


patient_portal.to_sql(TABLENAME, con=engine)
