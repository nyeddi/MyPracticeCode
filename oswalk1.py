import os
from os.path import join, getsize
for root, dirs, files in os.walk('C:\\Users\\ynaveenkumar\\Documents\\Tech-Books\\Python'):
            print root, "consumes",
            for dir in dirs:
                print dir
            for file in files:
                print file
