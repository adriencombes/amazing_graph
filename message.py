import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import os

upp_A = np.array([[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1]])
upp_B = np.array([[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,0]])
upp_H = np.array([[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]])
upp_W = np.array([[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,1,1,1,1],[1,1,0,1,1],[0,1,0,1,0]])
upp_W = np.array([[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1],[0,1,0,1,0]])

low_A = np.array([[0,0,0,0],[0,0,0,0],[0,1,1,0],[1,0,1,0],[1,0,1,0],[1,1,1,1],[0,0,0,0]])
low_D = np.array([[0,0,0],[0,0,1],[0,0,1],[0,1,1],[1,0,1],[1,0,1],[0,1,1]])
low_E = np.array([[0,0,0],[0,0,0],[0,0,0],[1,1,1],[1,1,1],[1,0,0],[1,1,1]])
low_H = np.array([[0,0,0], [1,0,0],[1,0,0],[1,1,1],[1,0,1],[1,0,1],[0,0,0]])
low_L = np.array([[0],[1],[1],[1],[1],[1],[1]])
low_O = np.array([[0,0,0],[0,0,0],[0,0,0],[1,1,1],[1,0,1],[1,0,1],[1,1,1]])
low_R = np.array([[0,0],[0,0],[0,0],[1,1],[1,0],[1,0],[1,0]])
low_W = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[0,1,0,1,0],[0,0,0,0,0]])

space = np.array([[0],[0],[0],[0],[0],[0],[0]])

message = np.concatenate((upp_H,space,
                           low_E,space,
                           low_L,space,
                           low_L,space,
                           low_O,space,
                           space,space,
                           upp_W,space,
                           low_O,space,
                           low_R,space,
                           low_L,space,
                           low_D),
                          axis=1)

rows_to_fill = 53 - message.shape[1]

message_filled = np.concatenate((message,np.zeros((7,rows_to_fill),dtype='int')),axis=1)
message_flat = list(message_filled.reshape(1,371,order='F')[0])
all_dates = []
active_dates = []
deltas = []

for d,p in enumerate(message_flat):
    delta = int(369-d)
    deltas.append(delta)
    day = datetime.now()-timedelta(days=delta)
    all_dates.append(day)
    if p == 1:
        active_dates.append(day)

days = []
for date in all_dates:
    days.append(date.strftime('%Y.%m.%d'))

def pretty(img):
    return img - (np.random.rand(7,53)/4)

commits = (pretty(message_filled+.25)*15).astype('int')

os.system('git status')
for n in range(len(message_flat)):
    commits = list(commits.reshape(1,371,order='F'))[0]
    if deltas[n] > 0:
        counter = 0
        while counter < commits[n]:
            with open('log.txt', 'a') as file:
                log = f'\n{str(deltas[n])} days ago - '
                log += f'date is {days[n]} - '
                log += f'commit {counter+1} / {commits[n]}'
                file.write(log)
            os.system('git add .')
            os.system(f'git commit --date="{days[n]}" -m "commit"')
            counter += 1
os.system('gh repo create --private --source=. --remote=upstream --push')
