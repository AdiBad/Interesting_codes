# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:19:41 2019

@author: Aditya
"""

import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


#text = "For visualization, matplotlib is a basic library that enables many other libraries to run and plot on its base including seaborn or wordcloud that you will use in this tutorial. The pillow library is a package that enables image reading. Its tutorial can be found here. Pillow is a wrapper for PIL - Python Imaging Library. You will need this library to read in image as the mask for the wordcloud.";
import io
f = io.open("sampletext_forwc.txt", mode="r", encoding="utf-8")
text = f.read();
f.close();

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

'''
#Increase size and clarity

wordcloud = WordCloud(width=800, height=400).generate(text)
plt.figure( figsize=(20,10) )
plt.imshow(wordcloud)

'''

from collections import Counter as c
import re
c(re.split(' |.',text)).most_common(17)