
import os
import shutil

shutil.copytree(os.path.join('..','amazing_graph'),os.path.join('..','le_repo'))
os.chdir(os.path.join('..','le_repo'))
shutil.rmtree('.git')
os.system('git init -b main')
os.system('python message.py')
