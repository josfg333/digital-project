import os

SECRET_KEY_FILENAME = "secretkey.dat"
BCRYPT_ROUNDS = 14

APP_DIR = os.path.dirname(os.path.abspath(__file__) ) #This is the directory of the project
PROJECTS_FOLDER = os.path.join(APP_DIR,"projects")