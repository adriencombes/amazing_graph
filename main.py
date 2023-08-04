
import os
import shutil
import sys

os.system('gh repo delete --confirm dont_name_me_like_that')
shutil.copytree(os.path.join('..','amazing_graph'),os.path.join('..','dont_name_me_like_that'))
os.chdir(os.path.join('..','dont_name_me_like_that'))
shutil.rmtree('.git')
os.system('git init -q -b main')
os.system(f'python message.py "{sys.argv[1]}"')
