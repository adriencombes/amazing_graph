import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import os
import pytz
import random
import shutil
import sys

text = sys.argv[1]

alphabet = {
'upp_A':np.array([[0,1,1,0],[1,0,0,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]]),
'upp_B':np.array([[1,1,1,0],[1,0,0,1],[1,0,0,1],[1,1,1,0],[1,0,0,1],[1,0,0,1],[1,1,1,0]]),
'upp_C':np.array([[0,1,1,0],[1,0,0,1],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,1],[0,1,1,0]]),
'upp_D':np.array([[1,1,0,0],[1,0,1,0],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,1,0],[1,1,0,0]]),
'upp_E':np.array([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,0],[1,0,0,0],[1,1,1,1]]),
'upp_F':np.array([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,0],[1,0,0,0],[1,0,0,0]]),
'upp_G':np.array([[0,1,1,0],[1,0,0,1],[1,0,0,0],[1,0,0,0],[1,0,1,1],[1,0,0,1],[0,1,1,0]]),
'upp_H':np.array([[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,0,0,1]]),
'upp_I':np.array([[1],[1],[1],[1],[1],[1],[1]]),
'upp_J':np.array([[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[1,0,0,1],[1,0,0,1],[0,1,1,0]]),
'upp_W':np.array([[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,1,1,1,1],[1,1,0,1,1],[0,1,0,1,0]]),
'upp_W':np.array([[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1],[0,1,0,1,0]]),

'low_A':np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[1,0,1,0],[1,0,1,0],[1,1,1,1]]),
'low_B':np.array([[0,0,0],[1,0,0],[1,0,0],[1,1,0],[1,0,1],[1,0,1],[1,1,0]]),
'low_C':np.array([[0,0,0],[0,0,0],[0,0,0],[0,1,1],[1,0,0],[1,0,0],[0,1,1]]),
'low_D':np.array([[0,0,0],[0,0,1],[0,0,1],[0,1,1],[1,0,1],[1,0,1],[0,1,1]]),
'low_E':np.array([[0,0,0],[0,0,0],[0,0,0],[1,1,1],[1,1,1],[1,0,0],[1,1,1]]),
'low_H':np.array([[0,0,0],[0,0,0],[1,0,0],[1,0,0],[1,1,1],[1,0,1],[1,0,1]]),
'low_I':np.array([[0],[0],[1],[0],[1],[1],[1]]),
'low_L':np.array([[0],[1],[1],[1],[1],[1],[1]]),
'low_M':np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1]]),
'low_N':np.array([[0,0,0],[0,0,0],[0,0,0],[1,1,1],[1,0,1],[1,0,1],[1,0,1]]),
'low_O':np.array([[0,0,0],[0,0,0],[0,0,0],[0,1,0],[1,0,1],[1,0,1],[0,1,0]]),
'low_R':np.array([[0,0],[0,0],[0,0],[1,1],[1,0],[1,0],[1,0]]),
'low_S':np.array([[0,0],[0,0],[0,0],[1,1],[1,0],[0,1],[1,1]]),
'low_T':np.array([[0,0,0],[0,0,0],[0,1,0],[1,1,1],[0,1,0],[0,1,0],[0,1,0]]),
'low_U':np.array([[0,0,0],[0,0,0],[0,0,0],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]),
'low_V':np.array([[0,0,0],[0,0,0],[0,0,0],[1,0,1],[1,0,1],[1,1,1],[0,1,0]]),
'low_W':np.array([[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[0,1,0,1,0],[0,0,0,0,0]]),
'low_Y':np.array([[0,0,0],[0,0,0],[0,0,0],[1,0,1],[1,0,1],[0,1,0],[1,0,0]]),
'low_Z':np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,1,0],[0,1,0,0],[1,1,1,1]]),

'space':np.array([[0],[0],[0],[0],[0],[0],[0]]),
'heart':np.array([[0,0,0,0,0,0,0],[0,1,1,0,1,1,0],[1,0,0,1,0,0,1],[1,0,0,0,0,0,1],[0,1,0,0,0,1,0],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0]])
}

def text_encoder(text):
    text_encoded = []
    for t in text:
        if t == ' ': t_encoded = 'space'
        elif t == '&': t_encoded = 'heart'
        else:
            t_encoded = 'upp_' if t.isupper() else 'low_'
            t_encoded += t.upper()
        text_encoded.append(t_encoded)
        text_encoded.append('space')

    for i, l in enumerate(text_encoded[:-1]):
        if not i: message = alphabet[l]
        else: message = np.concatenate([message,alphabet[l]],axis=1)
    return message

message = text_encoder(text)

if message.shape[1] < 53:
    rows_to_fill = 53 - message.shape[1]
    message_filled = np.concatenate((message,np.zeros((7,rows_to_fill),dtype='int')),axis=1)
else :
   message_filled = message[:,:53]
message_flat = list(message_filled.reshape(1,371,order='F')[0])

def print_message(array):
    message_string = ''
    for index, x in np.ndenumerate(message_filled):
        if x == 1: message_string += '██'
        else : message_string += '__'
        if index[1] == 52:
            message_string += '\n'
    print(message_string)
    pass

print_message(message_filled)

push = True
if push:

    all_dates = []
    active_dates = []
    deltas = []

    for d,p in enumerate(message_flat):
        delta = int(369-d)
        deltas.append(delta)
        day = datetime.now(pytz.timezone('Etc/GMT+0'))-timedelta(days=delta)
        all_dates.append(day)
        if p == 1:
            active_dates.append(day)

    days = []
    for date in all_dates:
        days.append(date.strftime('%Y.%m.%d'))

    commits = message_filled*(np.random.rand(7,53)*3+11).astype('int')

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
                os.system(f'git commit --date="{days[n]}" -m "{log}"')
                counter += 1
    os.system('gh repo create --private --source=. --remote=upstream --push')

shutil.rmtree(os.path.join('..','dont_name_me_like_that'))
