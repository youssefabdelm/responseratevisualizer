import nltk
from collections import Counter
from collections import OrderedDict
#from collections import defaultdict
import pandas as pd
from datetime import datetime, timedelta
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from matplotlib.cm import get_cmap
import matplotlib.font_manager as font_manager
from cycler import cycler
from matplotlib.pyplot import figure
from collections import defaultdict
from itertools import accumulate
import numpy as np
from nltk.corpus import stopwords
import string
import os
from itertools import tee, islice, chain
import PIL.Image
from PIL import Image
import PIL.ImageChops
import PIL.ImageOps
from PIL import ImageMath
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import re
import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def contains_word(s, w):
    return f' {w} ' in f' {s} '

filename = input('Input favorites filename with extension (e.g. filename.csv): ')
n = int(input("Enter number of words in a phrase: (e.g. 1: potato, 2: potato patata, 3: potato patata tamata): "))
limit = int(input("# of words to visualize in combination: (Input a number. Recommended: 17): ")) + 1
if n == 1:
    wordstoexclude = input("Input words to exclude from visualization (insert a space between each word): ").split()
elif n ==2:
    wordstoexclude = input("Input words to exclude from visualization (insert a comma between every 2 words): ").split(", ")
elif n ==3:
    wordstoexclude = input("Input words to exclude from visualization (insert a comma between every 3 words): ").split(", ")
twitterfile = pd.read_csv(filename)

#will do 2 words next
#1 word
def flatten(listoflists):
    flattenedlist = []
    for x in listoflists:
        for y in x:
            flattenedlist.append(y)
    return flattenedlist

def flattendouble(listoflists):
    flattenedlist = []
    for x in listoflists:
        for y in x:
            for z in y:
                flattenedlist.append(z)
    return flattenedlist

def flattendoubleskipfirst(listoflists):
    flattenedlist = []
    for x in listoflists[1:]:
        for y in x:
            for z in y:
                flattenedlist.append(z)
    return flattenedlist

stop_words = set(stopwords.words('english'))

alltweets = []
sometweets = []
sentencescombined = []
tweetscombined = []
for tweet in twitterfile["tweet"]:
    alltweets.append(tweet)
sentenceofeverytweet = []
tokensap = []
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
lemmatizer = nltk.stem.WordNetLemmatizer()


def get_ngrams(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]

def cleaning(sentences):
  words = []
  for s in sentences:

    #print()

    #s.replace('.','')
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", str(s).replace("'s"," is").replace("'re"," are"))
    #print(clean)

    w = get_ngrams(clean, n)
    #lemmatizing
    if n > 1:
        words.append([lemmatizer.lemmatize(i.lower()) for i in w])
    elif n == 1:
        words.append([i.lower() for i in w])

  return words


alltweetwords = []
sometweetwords = []

for sentence in alltweets:
    alltweetwords.append(sentence) #alltweetwords is array that contains every tweet as an array of words

#print(cleaning(alltweetwords))
alltweetwordsflattened = cleaning(alltweetwords) #flatten(alltweetwords)

allwordslowercase = []
allwordslowercase = alltweetwordsflattened


if n == 1:

    toremove = ["such", "based", "while","000","development","percent","she", "into", "world", "nan","his","these","them","had","were","where","because", "ly","its","ve","2019","2018","here","being","their","same","those","been","re","other","few","then","who","any","after","love", "up","your","watch","over","which","as","than","too","out","has","me","status","on","are","pic","have","from","or","an","be","is","by","will be","in the","of the","you ", " ","quite","'ll","system","stage","sort","pany","'ll'","'d'",'.',',',':',';','$','&',"’","...","@","!","?",")","(","http","https","…","%","''","'","would","will","yes","no","we","the","this","next","time","no","yeah","just","you","actually","sure","us","think","still","not","``","“","”","there","...","well","last","what","btw","done","like","good","it","'s","great","n't","one","that","people","also","first","much","high","soon","year","thanks","need","true","right","new","get","better","coming","even","probably","if","maybe","really","many","going","could","exactly","way","work","go","//myoutubecom/watch","myoutube/watch","week","best","almost","lot","test","back","know","point","ok","full","use","months","long","flight","cool","power","want","working","made","day","big","end","today","needed","air","something","take","real","around","cost","they","change","hard","make","see","speed","looks","less","far","so","always","definitely","days","10","may","every","already","haha","hopefully","all","enough","ever","max","safety","month","two","low","for","super","important","version","service","makes","order","and","small","little","due","free","video","in","several","never","to","weeks","please","things","amazing","should","sorry","early","worth","la","my","update","say","water","performance","fun","thing","problem","via","live","center","release","help","higher","times","miles","said","side","range","awesome","fast","look","pressure","might","public","course","start","control","life","mins","part","ship","yet","fire","support","media","later","am","def","per","without","goes","needs","must","hope","usig","add","try","using","//myoutubecom/watch","years","team","production","sounds","anything","major","rear","cape","idea","called","mass","possible","but","mission","gas","nothing","hours","top","money","tomorrow","anyone","owners","though","'m","level","lower","likely","pretty","looking","ago","got","vs","extremely","used","product","motor","welcome","mode","getting","station","price","three","deep","night","very","stop","read","wrong","100","clear","only","land","short","sense","review","value","fully","happy","come","now","20","half","thank","bad","companies","prob","about","twitter","ca","wow","interesting","option","especially","options","making","advanced","more","upgrade","roof","improve","place","zero","thought","front","can","name","means","some","trying","building","hardware","heat","believe","least","buy","away","forward","testing","aiming","close","our","fair","show","risk","sec","feature=youtube","♥️'","♥️","care","he","'re","upper","steel","body","move","current","open","able","texas","data","do","built","1st","another","technology","mostly","of","force","literally","easy","let","parts","case","how","someone","slightly","glad","question","reason","matter","30","person","most","city","1000","appreciated","set","find","road","longer","pack","fine","crazy","dual","seems","when","tax","critical","plus","record","actual","false","when","others","works","europe","at","ready","rate","size","'ve","unveil","fly","takes","access","tons","either","home","increase","prices","allow","costs","velocity","was",'return',"post","taking","exciting","base","single","online","difficult","correct","area","since","sound","weekend","bit","beyond","note","check","feel","red","yup","complete","seem","sales","core","recommend","took","meant","volume","vacuum","giant","target","within","why","wheel","cause","phone","give","computer","main","agree","mph","with","improvements","adding","designed","near","feature","everyone","whole","don","plan","ground","obv","oh","second","saying","wish","white","market","heard","mean","agreed","general","excellent","tonight","put","50","however","million","burn","nice","cover","final","room","oxygen","net","hot","run","owner","piece","currently","fuel","fixed","satellites","difference","tiny","line","credit","games","congratulations","60","smart","myoutube/watch"] #Add regularly occurring words here in this list
    for e in wordstoexclude:
        toremove.append(e)
#elif n == 2:
    #toremove = [" will",""]
elif n == 2:
    toremove = ['we bought','bought a','08 16','in 1st', 'com 2018', '2019 06', '2019 08', '2019 10', '2019 09', '2019 05', '2018 10', '3 is', '2019 03', '2019 04', '2019 06', '2019 07', '2019 08', '2019 10', '2019 11', '2019 12', '2019 02',"much more","than the","it has", "of its","according to", "well as", "cost of", "a bit","here s", "you ll", "them to", "and then", "be able", "what we", "lots of", "even more", "and what", "so many", "i believe", "to go", "opportunity to", "what i", "ve been", "ability to", "when we", "and their","trying to", "of what", "has a", "about what", "are the", "are a", "in my", "a better", "not only", "their own", "the other", "they were", "more about", "a year", "ll be", "the new", "a very", "and in", "but we", "it would", "as we", "we were", "you ll"  "thousands of", "that can", "up to", "to meet", "make a", "as well", "ways to", "to work", "s not", "i ll", "i hope", "of all", "was the", "and more", "the right", "a huge", "i d", "s the", "to use", "how the", "time to", "could be", "how much", "make the","look at", "the number", "is an", "kind of", "of them", "that they", "as i", "at a", "to take", "isn t", "of his", "of this", "because of", "the people", "such as", "like the", "you have", "chance to", "the time", "in their", "a good", "talk about", "and how", "they have", "last year", "what s", "into the", "many of", "he was", "and they", "the united", "they can", "and that", "he s", "she s", "t have", "have the", "had a", "and we", "of my", "is one", "to have", "the past", "of their", "to improve", "that will", "if we", "most of", "of these", "who are", "that it", "all of", "if it", "of these", "percent of", "the way", "that i", "as the", "i have", "years ago", "people in", "i am", "we ve", "able to", "is to", "but the", "access to", "of our", "the last", "millions of", "i had", "the global","have been", "and it", "about how", "a big", "they are", "was a", "that are", "and a", "out of", "in this","can be", "have to", "the u", "they re", "how to", "people who", "of people", "this year", "when i", "way to","and other", "that we", "number of", "want to", "the next", "we need", "the same", "part of", "there s", "a great", "for example", "the best", "has been", "around the","and i", "about the", "more than", "i was", "that the", "we can", "to help", "some of", "there are", "u s", "by the", "with a", "over the", "we have", "the first", "world s",'you are', 'bit ly', 'all the', 'the most', 'i ve', 'and the', 'a new', 'when you', 'what you','twitter com', 'pic twitter', 'https twitter', 'will be', 'of the', 'https www', 'in the', 'to be', 'http www', 'it is', 'this is', 'is a', 'https m', 'm youtube', 'that is', 'to the', 'com p', 'on the', 'in a', 'watch v', 'for the', 'i m', 'don t', 'on the', 'in a', 'it s', 'youtube com', 'com watch', 'should be', 'instagram com', 'is the', 'that s', 'would be', 'if you', 'www instagram', 'need to', 'a lot', 'a few', 'can t', 'for a', 'you re', 'doesn t', 'to do', 'we re', 'is not', 'you can', 'we are', 'of a', 'there is', 'to make', 'we will', 'it will', 'won t', 'going to', 'lot of', 'youtu be', 'didn t', 'which is', 'i think', 'on a', 'like a', 'end of', 'have a', 'due to', 's a', 'next year', 'at the', 'but i', 'it was', 'be a', 'of course', 'to a', 'from the', 'but it', 'one of', 'thanks for', 'with the', 'will do', 'next week', 'as a', 'the world', 'to see', 'to get', 'is that', 'working on', 'com 2019', ''
    ] #Add regularly occuring bigrams
    for e in wordstoexclude:
        toremove.append(e)
elif n == 3:
    toremove = ['for the first', 'to try to', 'top of the', 't want to', 'as part of', 'in addition to', 'to do so','if you have', 'the top of', 'by the way', 'but that s', 'to get a', 'much of the', 'due to the', 'first of all', 'if you are', 'at the top', 'that i think', 'you have to','s hard to', 'it s hard', 'back to the', 'this is the', 'to have a','the past week', 'are going to', 'don t know','i didn t', 'is that it', 'of thousands of', 'it s also', 'a ton of', 'more and more', 'we ll see', 'as you can', 'that s the', 'but i think', 'that s a', 'by the end', 'it doesn t', 'but it is', 'that it is', 'as a whole','a bit more', 'according to the', 'as a whole', 'as much as', 'don t think', 'a handful of', 'don t think', 'there are a','here are some','i think the','in other words','a lot more','to be the', 'the us and','i m sure', 'seems to be','end of the', 'is that the', 'check out the', 'the company s','in the first', 'all of the', 'a bit of', 'iframe style height','it comes to', 'is expected to', 'think it s','originally published on', 'i m not', 'of the year', 'style height a', 'height a data', 'is going to', 'out of the', 'at the end', 'i think it', 'here s the', 'when it comes', 'going to be', 'in terms of', 'in the coming', 'if you want', 'in order to', 'the end of', 'a couple of', 'here s a', 'the cost of', 'we have to', 'the same time', 'the history of', 'is a great', 'the people who', 'people who are', 'to see the', 'it was a', 'of the best', 'the country s', 'i ll be', 'it will be', 'to improve the', 'a way to', 'a group of', 'they need to', 'there s no', 'as a result','percent of the','you don t', 'people in the', 'that it s', 'in the future', 'the world has', 'it s the', 'learn more about', 'to make a', 'i had a', 'at the same', 'it would be','when i was', 'it is a', 'over the next', 'but it s', 'in the u', 'many of the', 'and it s', 'i want to', 'to make the', 'to talk about', 'the most important', 'a few years', 'i ve been', 'the first time', 'of millions of', 'to make sure', 'look at the', 'a lot about', 'the rest of', 'over the last', 'to be a', 'they don t', 'you want to', 'need to be', 'the fact that', 'most of the','that s why', 'there s a', 'a chance to', 'as well as', 'we don t', 'this is a', 'in the past','be able to', 'part of the', 'don t have', 'i don t', 'that s why ', 'if you re', 'a number of', 'it s not','a lot of', 'one of the', 'the world s', 'the u s', 'in the world', 'some of the', 'of the world', 'we need to', 'it s a', 'of the most', 'the number of', 'is one of','pic twitter com', 'https twitter com', 'http bit ly', 'https youtu be'] #Add regularly occuring trigrams
    for e in wordstoexclude:
        toremove.append(e)
elif n == 4:
    toremove = ['of the most important', 'a lot of the','one of the most', 'is one of the', 'of the world s', 'at the same time', 'when it comes to', 'had a chance to', 'for the first time', 'a lot of time', 'one of the best', 'if you want to']
else:
    toremove = []
allwordscleaned = []

def checkifnumber(word):
    try:
        int(word)
    except ValueError:
        return False
    else:
        return True
def checkifletters(string):
    total = 0
    for letter in string.split(' '):
        total+= len(letter)

    if total == len(string.split(' ')):
        return True
    else:
        return False

if int(n) == 1:
    allwordslowerflattened = flatten(allwordslowercase)
    for word in allwordslowerflattened:
        if isinstance(word, list):
            raise ValueError('word is list')

        #print(word)
        if word not in toremove:
            if checkifnumber(word.replace(' ','').strip()):
                continue

            else:
                allwordscleaned.append(word)
elif n > 1:
    allwordslowerflattened = flatten(allwordslowercase)
    for words in allwordslowerflattened:
        if words not in toremove:
            if checkifnumber(words.replace(' ','').strip()):
                if checkifletters(words):
                    continue
                continue
            elif checkifletters(words):
                continue
            else:
                allwordscleaned.append(words)



allwordstemp = []
allwordsmorethanonecharacter = []
if n == 1:
    for word in allwordscleaned:

        if n == 1:
            if len(word) > 1:

                morethanonecharacter = word.replace('myoutube/watch','').replace('com','').replace('//','').replace('www','').replace('.','').replace(',','').replace(':','').replace('$','').replace('&','').replace('’','').replace("...","").replace("@","").replace("!","").replace("?","").replace("(","").replace(")","").replace("https","").replace("http","")
                allwordstemp.append(morethanonecharacter)

    for w in allwordstemp:
        if w not in toremove:
            if w != '':
                allwordsmorethanonecharacter.append(w)

elif n > 1:
    allwordsmorethanonecharacter = allwordscleaned

print(allwordsmorethanonecharacter)

counted = OrderedDict(Counter(allwordsmorethanonecharacter).most_common(limit))

print(counted)


plt.style.use('seaborn')



dictofdatesandtweets = {}
dictoftweetsanddates = {}
dictofcounts = {}
listofd = []
listoflistofwordsintweet = []
listofwordsintweet = []

def cleaned(s):
    cleaneds = s.replace('myoutube/watch','').replace('com','').replace('//','').replace('www','').replace('.','').replace(',','').replace(':','').replace('$','').replace('&','').replace('’','').replace("...","").replace("@","").replace("!","").replace("?","").replace(")","").replace("(","").replace("https","").replace("http","")
    if len(cleaneds) < 1:
        cleaneds = 'the'
    return str(cleaneds)

def tokenizelist(listofstrings):
    #this function tokenizes a list of strings into one words and makes all words lowercase
    listoftokenizedwords = []
    for string in listofstrings:
        listoftokenizedwords.append(nltk.word_tokenize(string.lower()))
    ftokenizedwords = flatten(listoftokenizedwords)
    return ftokenizedwords


dictofwordsanddates = {}
items = list(twitterfile["date"])
l = len(items)
printProgressBar(0, l, prefix = 'Combining dates and words:', suffix = 'Complete', length = 50)
for i, date in enumerate(twitterfile["date"]):
    dictofdatesandtweets.update({date:tuple(flatten(cleaning(twitterfile['tweet'][twitterfile[twitterfile['date'] == date].index.tolist()].tolist())))})
    #time.sleep(0.00001)
    printProgressBar(i + 1, l, prefix = 'Combining dates and words:', suffix = 'Complete', length = 50)

print(dictofdatesandtweets)
dictofwordsandtweets = {}
dictofwords = {}
dictofdatestweetswords = {}
count = 0
somewordslowercase = []
sometweetslist = []
dictofwordsanddates = {}
finaldictofwords = {}

#styling - fonts
name = "tab20"
pathofthinfont = "fonts/GT-America-Expanded-Thin.OTF"
pathoflightfont = "fonts/GT-America-Expanded-Light.OTF"
pathofregularfont = "fonts/GT-America-Expanded-Regular.OTF"
path = 'fonts/GT-America-Extended-Medium.OTF'
font = font_manager.FontProperties(fname=path)

plt.figure(figsize=(16,9))

cmap = get_cmap(name)  # type: matplotlib.colors.ListedColormap
colors = cmap.colors  # type: list
plt.rc('axes', prop_cycle=(cycler('color', colors)))
latestdate = twitterfile['date'][0] #latest tweet date

fontthin = font_manager.FontProperties(fname=pathofthinfont)
fontlight = font_manager.FontProperties(fname=pathoflightfont)
fontregular = font_manager.FontProperties(fname=pathofregularfont)

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

items = list(counted.keys())
l = len(items)

printProgressBar(0, 1, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, ccword in enumerate(counted.keys()):
    ccworddateslist = []
    for key, value in dictofdatesandtweets.items():

        valuecounted = OrderedDict(Counter(value).most_common())
        if ccword in value:

            print('found ', ccword, valuecounted.get(ccword), value, key)
            #another idea here: de-indent iffccword below, and append above information to a list or dict for every user later to be used
            ccworddateslist.append([key]*valuecounted.get(ccword))

    finaldictofwords.update({ccword:list(reversed(list(flatten(ccworddateslist))))})
    #time.sleep(0.00001)
    printProgressBar(i + 1, l, prefix = "Progress:", suffix = 'Complete', length = 50)
print(finaldictofwords)

limitnum = int(limit)

for term in list(finaldictofwords.keys()):
    listofdatesforeveryterm = finaldictofwords.get(term)
    counteddates = OrderedDict(Counter(listofdatesforeveryterm))
    if not latestdate in counteddates.keys():
        print('latestdate not found, adding latest date with 0. latest date is: ', latestdate)
        counteddates.update({latestdate: 0})
    cumulativecounts = list(accumulate(list(counteddates.values())))
    dateslist = [datetime.strptime(date, '%Y-%m-%d').date() for date in counteddates.keys()]
    plt.legend(prop=font)
    plt.step(dateslist, cumulativecounts, linestyle='solid', linewidth=0.5, label=(term + '\n' + str(counted.get(term)) + ' ' + 'mentions'))
ax = plt.axes()
for label in ax.get_xticklabels():
    label.set_fontproperties(fontregular)
    #ax.set_fontproperties(font)
for label in ax.get_yticklabels():
    label.set_fontproperties(fontregular)

name = str(filename).replace('.csv','')
if not os.path.exists('schedules/'):
    os.mkdir('schedules/')
if not os.path.exists('schedules/' + 'for ' + str(name) + ' terms'):
    os.mkdir('schedules/' + 'for ' + str(name) + ' terms')
plt.savefig('schedules/' + 'for ' + str(name) + ' terms' + '/Top ' + str(int(limit) - 1) + ' ' + str(n) + ' terms for ' + name + ' latest occurence date ' + str(latestdate) + '.png',dpi=600)
name = str(filename).replace('.csv','')

if os.path.exists('schedules/' + 'for ' + str(name) + ' terms' + '/Top ' + str(int(limit) - 1) + ' ' + str(n) + ' terms for ' + name + ' latest occurence date ' + str(latestdate) + '.png'):
    filetoinvert = Image.open('schedules/' + 'for ' + str(name) + ' terms' + '/Top ' + str(int(limit) - 1) + ' ' + str(n) + ' terms for ' + name + ' latest occurence date ' + str(latestdate) + '.png')

    r,g,b,a = filetoinvert.split()
    rgb_image = Image.merge('RGB', (r,g,b))

    inverted_image = PIL.ImageOps.invert(rgb_image)

    r2,g2,b2 = inverted_image.split()

    final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
    if not os.path.exists('schedules/' + 'for ' + str(name) + ' terms/' + 'black-schedules'):
        os.mkdir('schedules/' + 'for ' + str(name) + ' terms' + '/' + 'black-schedules')

    final_transparent_image.save('schedules/' + 'for ' + str(name) + ' terms' + '/' + 'black-schedules' + '/Top ' + str(int(limit) - 1) + ' ' +  str(n) + ' terms for ' + name + ' latest occurence date ' + str(latestdate) + '.png')


continueornot = input("Continue to top individual terms schedules? Press Enter ")

for term in list(finaldictofwords.keys()):
    listofdatesforeveryterm = finaldictofwords.get(term)
    counteddates = OrderedDict(Counter(listofdatesforeveryterm))
    if not latestdate in counteddates.keys():
        print('latestdate for ' + str(term) + ' not found, adding latest date with 0. latest date is: ', latestdate)
        counteddates.update({latestdate: 0})
    cumulativecounts = list(accumulate(list(counteddates.values())))
    dateslist = [datetime.strptime(date, '%Y-%m-%d').date() for date in counteddates.keys()]
    plt.figure(figsize=(16,9))
    plt.step(dateslist, cumulativecounts, linestyle='solid', linewidth=0.5, label=(term + '\n' + str(counted.get(term)) + ' ' + 'mentions'))
    plt.legend(prop=font)
    ax = plt.axes()
    for label in ax.get_xticklabels():
        label.set_fontproperties(fontregular)
        #ax.set_fontproperties(font)
    for label in ax.get_yticklabels():
        label.set_fontproperties(fontregular)


    name = str(term)
    if not os.path.exists('schedules/'):
        os.mkdir('schedules/')
    if not os.path.exists('schedules/' + 'for ' + str(filename).replace('.csv','') + ' terms'):
        os.mkdir('schedules/' + 'for ' + str(filename).replace('.csv','') + ' terms')
    #plt.show()
    plt.savefig('schedules/' + 'for ' + str(filename).replace('.csv','') + ' terms' + '/' + name + ' latest occurence date ' + str(latestdate) + '.png',dpi=600)

    if os.path.exists('schedules/' + 'for ' + str(filename).replace('.csv','') + ' terms' + '/' + name + ' latest occurence date ' + str(latestdate) + '.png'):
        filetoinvert = Image.open('schedules/' + 'for ' + str(filename).replace('.csv','') + ' terms' + '/' + name + ' latest occurence date ' + str(latestdate) + '.png')

        r,g,b,a = filetoinvert.split()
        rgb_image = Image.merge('RGB', (r,g,b))

        inverted_image = PIL.ImageOps.invert(rgb_image)

        r2,g2,b2 = inverted_image.split()

        final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
        if not os.path.exists('schedules/' + 'for ' + str(filename).replace('.csv','') + ' terms/' + 'black-schedules'):
            os.mkdir('schedules/' + 'for ' + str(filename).replace('.csv','') + ' terms' + '/' + 'black-schedules')

        final_transparent_image.save('schedules/' + 'for ' + str(filename).replace('.csv','') + ' terms' + '/' + 'black-schedules' + '/' + name + ' latest occurence date ' + str(latestdate) + '.png')
