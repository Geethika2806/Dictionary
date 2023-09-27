#!/usr/bin/env python
# coding: utf-8

# In[1]:



import json
from difflib import get_close_matches

while True:

    data = json.load(open("data.json"))

    def translate(w):
        w=w.lower()
        if w in data:
            return data[w]
        elif w.capitalize() in data:
             return data[w.capitalize()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w,data.keys())) > 0:
            yn= input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w,data.keys())[0])
            if yn == "Y":
                return data[get_close_matches(w,data.keys())[0]]
            elif yn == "N":
                 return "The word doesn't exist.Please double check it"
            else:
                return "We didn't understand your entry"

        else:
            return "The word doesn't exist.Please double check it"

    word=input("Enter a word: ")

    output=translate(word)

    if isinstance(output,list):
        for items in output:
            print(items)

    else:
        print(output)











# In[ ]:




