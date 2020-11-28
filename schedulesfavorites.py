import pandas as pd
from datetime import datetime, timedelta
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from matplotlib.cm import get_cmap
import matplotlib.font_manager as font_manager
from cycler import cycler
from matplotlib.pyplot import figure
from collections import OrderedDict
from collections import Counter
from collections import defaultdict
from itertools import accumulate
import PIL.Image
from PIL import Image
import PIL.ImageChops
import PIL.ImageOps
from PIL import ImageMath
import numpy as np
import altair as alt
from vega_datasets import data
import os

#this is a function to flatten a list of lists
def flatten(listoflists):
    flattenedlist = []
    for x in listoflists:
        for y in x:
            flattenedlist.append(y)
    return flattenedlist
plt.style.use('seaborn')


filename = input('Input favorites filename with extension (e.g. filename.csv): ')
limityn = input("Limit total visualization to custom number of users? (Faster+Looks better) Input: y/n : ")

if limityn == "y":
    limit = input("Top x users to visualize in combination: (Input a number): ")
numlabel = input("What should the label for the legend be? (e.g. 186 'likes' or 186 'retweets' or 186 'mentions'). Input a label: ")
favorites = pd.read_csv(filename)

dictofdatesandusers = {}
dictofusersanddates = {}
for user in favorites["username"]:
    dictofusersanddates.update({user:favorites['date'][favorites[favorites['username'] == user].index.tolist()].tolist()})


for date in favorites["date"]:

    dictofdatesandusers.update({date:favorites['username'][favorites[favorites['date'] == date].index.tolist()].tolist()})
print(dictofdatesandusers)

counted = OrderedDict(Counter(flatten(dictofdatesandusers.values())).most_common())

dictofdatesandcounts = {}

name = "tab20"
pathofthinfont = "fonts/GT-America-Expanded-Thin.OTF"
pathoflightfont = "fonts/GT-America-Expanded-Light.OTF"
pathofregularfont = "fonts/GT-America-Expanded-Regular.OTF"
path = 'fonts/GT-America-Extended-Medium.OTF'
#if int(limit) <= 17:
font = font_manager.FontProperties(fname=path)

fontthin = font_manager.FontProperties(fname=pathofthinfont)
fontlight = font_manager.FontProperties(fname=pathoflightfont)
fontregular = font_manager.FontProperties(fname=pathofregularfont)

print("Now exporting top " + str(limit) + " users")
if limityn == "y":


    plt.figure(figsize=(16,9))

    cmap = get_cmap(name)  # type: matplotlib.colors.ListedColormap
    colors = cmap.colors  # type: list
    plt.rc('axes', prop_cycle=(cycler('color', colors)))
    latestdate = favorites['date'][0]
    limitnum = int(limit) + 1
    for index, user in zip(range(int(limitnum)), counted.keys()):
        print(index, user)
        listofdatesforeveryuser = list(reversed(dictofusersanddates.get(user)))
        counteddates = OrderedDict(Counter(listofdatesforeveryuser))
        if not latestdate in counteddates.keys():
            counteddates.update({latestdate: 0})
        cumulativecounts = list(accumulate(list(counteddates.values())))


        print(counteddates.keys())
        dateslist = [datetime.strptime(date, '%Y-%m-%d').date() for date in counteddates.keys()]
        print(user, dateslist)


        if int(limit) <= 17:
            plt.legend(prop=font)
        elif int(limit) > 17:
            plt.legend(fontsize=6)

            plt.legend(prop=font)





        plt.step(dateslist, cumulativecounts, linestyle='solid', linewidth=0.5, label=(user + '\n' + str(counted.get(user)) + ' ' + numlabel)) # in for d, u for first run, going to shove it back to see what happens



    ax = plt.axes()
    for label in ax.get_xticklabels():
        label.set_fontproperties(fontregular)
    for label in ax.get_yticklabels():
        label.set_fontproperties(fontregular)


    name = str(filename).replace('.csv','')
    if not os.path.exists('schedules/' + 'for ' + str(name)):
        os.mkdir('schedules/' + 'for ' + str(name))
    plt.savefig('schedules/' + 'for ' + str(name) + '/Top ' + str(limit) + ' users for ' + name + ' latest recorded date ' + str(latestdate) + '.png',dpi=600)
    if os.path.exists('schedules/' + 'for ' + str(name) + '/Top ' + str(limit) + ' users for ' + name + ' latest recorded date ' + str(latestdate) + '.png'):
        filetoinvert = Image.open('schedules/' + 'for ' + str(name) + '/Top ' + str(limit) + ' users for ' + name + ' latest recorded date ' + str(latestdate) + '.png')

        r,g,b,a = filetoinvert.split()
        rgb_image = Image.merge('RGB', (r,g,b))

        inverted_image = PIL.ImageOps.invert(rgb_image)

        r2,g2,b2 = inverted_image.split()

        final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
        if not os.path.exists('schedules/' + 'for ' + str(name) + '/' + 'black-schedules'):
            os.mkdir('schedules/' + 'for ' + str(name) + '/' + 'black-schedules')

        final_transparent_image.save('schedules/' + 'for ' + str(name) + '/' + 'black-schedules' + '/Top ' + str(limit) + ' users for ' + name + ' latest recorded date ' + str(latestdate) + '.png')




input("Continue to plotting individual users? Press Enter if yes or Ctrl-C if not.")

for user in counted.keys():

    path = 'fonts/GT-America-Extended-Medium.OTF'
    font = font_manager.FontProperties(fname=path)

    mpl.rcParams['font.family'] = font.get_name()
    mpl.rcParams['font.stretch'] = 'ultra-expanded'
    mpl.rcParams['font.weight'] = 'regular'


    listofdatesforeveryuser = list(reversed(dictofusersanddates.get(user)))
    counteddates = OrderedDict(Counter(listofdatesforeveryuser))
    if not latestdate in counteddates.keys():
        counteddates.update({latestdate: 0})
    cumulativecounts = list(accumulate(list(counteddates.values())))

    dateslist = [datetime.strptime(date, '%Y-%m-%d').date() for date in counteddates.keys()]
    print(user, dateslist)
    plt.figure(figsize=(16,9))

    plt.step(dateslist, cumulativecounts, linestyle='solid', linewidth=0.5, label=(user + '\n' + str(counted.get(user)) + ' ' + numlabel)) # in for d, u for first run, going to shove it back to see what happens
    #plt.legend(prop={'size': 40})
    plt.legend(prop=font)
    if not os.path.exists('schedules/' + 'for ' + str(name)):
        os.mkdir('schedules/' + 'for ' + str(name))
    plt.savefig('schedules/' + 'for ' + str(name) + '/' + str(user) + ' latest recorded date ' + str(latestdate) + '.png',dpi=600)
    if os.path.exists('schedules/' + 'for ' + str(name) + '/' + str(user) + ' latest recorded date ' + str(latestdate) + '.png'):
        filetoinvert = Image.open('schedules/' + 'for ' + str(name) + '/'  + str(user) + ' latest recorded date ' + str(latestdate) + '.png')

        r,g,b,a = filetoinvert.split()
        rgb_image = Image.merge('RGB', (r,g,b))

        inverted_image = PIL.ImageOps.invert(rgb_image)

        r2,g2,b2 = inverted_image.split()

        final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
        if not os.path.exists('schedules/' + 'for ' + str(name) + '/' + 'black-schedules'):
            os.mkdir('schedules/' + 'for ' + str(name) + '/' + 'black-schedules')
            final_transparent_image.save('schedules/' + 'for ' + str(name) + '/' + 'black-schedules/' + str(user) + ' latest recorded date ' + str(latestdate) + '.png')
        else:
            final_transparent_image.save('schedules/' + 'for ' + str(name) + '/' + 'black-schedules/' + str(user) + ' latest recorded date ' + str(latestdate) + '.png')
