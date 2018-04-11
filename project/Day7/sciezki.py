import os, sys
from pprint import pprint

print('aktualny folder roboczy', os.getcwd())
print('foldery robocze Python:')
pprint(sys.path)

import bs4
