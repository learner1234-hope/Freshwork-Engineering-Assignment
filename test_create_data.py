import json

import fcntl 

import threading

from os import path

from datetime import datetime, timedelta

from sys import exit

from argparse import ArgumentParser

from configs import configurations

from utils.filehandler import Fp 

parser = ArgumentParser ()

parser.add_argument('--datastore', help = 'Enter the datastore absolute path.')

args = parser.parse_args()

if args.datastore:
 {
   db_path = args.datastore
 }
else:
 {
   db_path = configurations.DEFAULT_DB_PATH
 }
directory_created = Fp(db_path).create_folder() 
if not directory_created: 
   print(f"Permission denied: You can not create the directory '{db_path}'.\n") 
   exit(0)

json_data = {

"pqr": {

"data": "value1",

"data2": "value2",

"data3": "value3",

"Time-To-Live": 5000,

},

"abc": {

"data": "value1",

"data2": "value2",

"data3": "value3",

"Time-To-Live": 250,

},

"tuv": {

"data1": "value1",

"data2": "value2",

"data3": "value3",
 
"Time-To-Live": 300,

},

"xyz": {

"data1": "value1",

"data2": "value2",

"data3": "value3",

"Time-To-Live": 500,

}

}

''' CREATE DATA IN DATASTORE '''

_valid_data, message = DataStoreCRD().check_create_data(json_data, db_path)


print(message)


