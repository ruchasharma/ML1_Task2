#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Rucha Ramesh Sharma
# Student id - 101411277

import os
import requests
import re
from bs4 import BeautifulSoup

# In[2]:


# function to get the html source text of the medium article
import sys


def get_page():
    global url
    url = input('Enter the Medium Article URL for web scrapping:  ')
    if not re.match(r'https?://medium.com/', url):
        print('Please enter a valid website, or make sure it is a medium article')
        url = input('Enter the Medium Article URL for web scrapping:  ')
        sys.exit(1)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


# In[3]:


# function to remove all the html tags and replace some with specific strings
def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>": "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub('\<(.*?)\>', '', text)
    return text


# In[4]:


def collect_text(soup):
    text = f'url: {url}\n\n'
    para_text = soup.find_all('p')
    print(f"paragraphs text = \n {para_text}")
    for para in para_text:
        text += f"{para.text}\n\n"
    return text


# In[6]:


# function to save file in the current directory
def save_file(text):
    if not os.path.exists('./scraped_articles'):
        os.mkdir('./scraped_articles')
    name = url.split("/")[-1]
    print(name)
    fname = f'scraped_articles/{name}.txt'

    with open(fname, 'w') as file:  # Use file to refer to the file object
        file.write(text)
    # Code ends here

    print(f'File saved in directory {fname}')


if __name__ == '__main__':
    text = collect_text(get_page())
    save_file(text)

# In[ ]:




