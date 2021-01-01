import json

import fcntl

import threading

from os import path

from datetime import datetime, timedelta

from dateutil.parser import parse

from configs.configurations import DEFAULT_

class DataStoreCRD:

    def check_time_to_live(self, value): 

         created_time = value['CreatedAt']

         created_time = parse(created_time)

         time_to_live = value['Time-To-Live']

         if time_to_live is not None:  
    
              expired_datetime = created_time