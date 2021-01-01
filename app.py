from sys import exit

from flask import Flask

from argparse import ArgumentParser

from configs import settings, configuration

from utils.filehandler import Fp

from CRD.views import CreateData, ReadData, DelData

parser = ArgumentParser()

parser.add_argument('--datastore', help='Enter the datastore absolute path')

args = parser.parse_args()

if args.datastore:

   db_path = args.datastore 

else:

   db_path = configurations.DEFAULT_DB_PATH

directory created = Fp(db_path).create_folder()

if not directory_created:

print(f"Permission denied: Can't create the directory '{db_path}'.\n")

exit(0)

app = Flask(_name_)

app.config['DEBUG'] = settings.DEBUG

app.config['SECRET_KEY'] = settings. SECRET_KEY

if_name_ == 'main':

  app.run(host=settings. HOST, port=settings.PORT)