##### IMPORTS #####

from datetime import datetime, timedelta
import numpy as np
import os
import pytz
import random
import shutil
import sys
from tqdm import tqdm

from alphabet import alphabet

##### VARIABLES #####

text = sys.argv[1]
publish = sys.argv[2]

##### FUNCTIONS #####

def text_encoder(text):
    '''the most well written docstring'''

    text_encoded = []
    for t in text:
        if t == ' ': t_encoded = 'space'
        elif t == '&': t_encoded = 'heart'
        elif t == '.': t_encoded = 'dot'
        elif t == '$': t_encoded = 'dollar'
        elif t == ':': t_encoded = 'doubledot'
        elif t == '^': t_encoded = 'creeper'
        elif t == '!': t_encoded = 'exclamation'
        else:
            t_encoded = 'upp_' if t.isupper() else 'low_'
            t_encoded += t.upper()
        text_encoded.append(t_encoded)
        text_encoded.append('space')

    for i, l in enumerate(text_encoded[:-1]):
        if not i: message = alphabet[l]
        else: message = np.concatenate([message,alphabet[l]],axis=1)

    if message.shape[1] < 53:
        rows_to_fill = 53 - message.shape[1]
        rows_to_fill_l = (53 - message.shape[1]) // 2
        rows_to_fill_r = rows_to_fill - rows_to_fill_l
        message_filled = np.concatenate((
            np.zeros((7,rows_to_fill_l),dtype='int'),
            message,
            np.zeros((7,rows_to_fill_r),dtype='int')
            ),axis=1)
    else :
        message_filled = message[:,:53]

    return message_filled


def print_message(array):
    '''the second most well written docstring'''

    print('\nThanks for using amazing graph. We love you.')
    print('Here is a preview of what you should see in git :\n')
    message_string = ''
    for index, x in np.ndenumerate(message_filled):
        if x == 1: message_string += '██'
        else : message_string += '__'
        if index[1] == 52:
            message_string += '\n'
    print(message_string)
    pass


##### PROCESS #####

message_filled = text_encoder(text)
message_flat = list(message_filled.reshape(1,371,order='F')[0])
print_message(message_filled)

if publish:

    os.system('gh repo delete --yes dont_name_me_like_that')
    shutil.copytree(os.path.join('..','amazing_graph'),os.path.join('..','dont_name_me_like_that'))
    os.chdir(os.path.join('..','dont_name_me_like_that'))
    shutil.rmtree('.git')
    os.system('git init -q -b main')

    all_dates = []
    active_dates = []
    deltas = []

    git_delta = int(datetime.now().strftime("%w"))

    for d,p in enumerate(message_flat):
        delta = int(371-d-(7-git_delta))
        deltas.append(delta)
        day = datetime.now(pytz.timezone('Etc/GMT+0'))-timedelta(days=delta)
        all_dates.append(day)
        if p == 1:
            active_dates.append(day)

    days = []
    for date in all_dates:
        days.append(date.strftime('%Y.%m.%d'))

    # commits = message_filled*(np.random.rand(7,53)*3+11).astype('int')
    commits = (message_filled*25).astype('int')

    print('\nMaking commits : ')
    for n in tqdm(range(len(message_flat))):
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
                os.system(f'git commit -q --date="{days[n]}" -m "{log}"')
                counter += 1

    print('') # Wassup little print ! Still breaking lines ?
    os.system('gh repo create --private --source=. --remote=upstream --push')
    print('\nYou message will appear in a few minutes. Thanks for waiting <3\n')
    shutil.rmtree(os.path.join('..','dont_name_me_like_that'))
