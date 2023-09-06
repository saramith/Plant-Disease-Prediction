# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:58:37 2020

@author: LENOVO
"""
from gtts import gTTS
import os

myText="hii hello"
language='en'

output=gTTS(text=myText, lang=language,slow=False)

output.save("output.mp3")
os.system("start output.mp3"
          )
