#!/usr/bin/python3
"""
file of number of subscribers method
"""
import re
import requests


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    len = sorted(dictionary.items(), key=lambda kv: kv[1])
    len.reverse()

    if len(len) != 0:
        for item in len:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
