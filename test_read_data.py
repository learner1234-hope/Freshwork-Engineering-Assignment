from sys import exit

from argparse import ArgumentParser

from configs import configurations

from utils.filehandler import FilePreprocess

from CRD. functions import DataStoreCRD

parser = ArgumentParser ()

parser.add_argument('--datastore', help='Enter the datastore absolute path.')

args = parser.parse_args()

if args.datastore:
     { 
       DB_PATH = args.datastore 
     }
else:
     {
       DB_PATH = configurations.DEFAULT_DB_PATH
     }
directory created = File Preprocess(DB_PATH).create_folder()

if not directory_created:

print(f"Permission denied: You can not create the directory '{DB_PATH}' .\n")

exit(0)

key = 'tuv'

'''READ DATA FROM DATASTORE'''

_data_found, message = DatastoreCRD().check_read_data(key, DB_PATH)
print(message)