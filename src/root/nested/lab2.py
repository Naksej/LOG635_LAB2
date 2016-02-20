import codecs
import re
import nltk
import nltk.data
#Pour importer des textes utilisable par la suite.
#http://www.nltk.org/book/ch01.html
#from nltk.book import *

# -*- coding: utf-8 -*-
from nltk import *

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

with open ("exemple2.cfg", "r") as myfile:
    grammaireText=myfile.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = nltk.ChartParser(grammar)
parser = parse.FeatureEarleyChartParser(grammar)

fp = open("Einstein.txt")
data = fp.read()
tokenisedData = tokenizer.tokenize(data);

#Enlever commentaire pour voir toute les phrase du texte
#print("\n-----\n".join(tokenizer.tokenize(data)))

#Exemple de token qui marche avec la grammaire de l'Exemple
#tokens = "Jean tua Marie avec une corde".split()

#Essaie pour la premiere phrase
tokens = tokenisedData[1].split()
trees = parser.parse(tokens)
for tree in trees:
    print(tree)
    nltk.draw.tree.draw_trees(tree)
    print(tree.label()['SEM'])