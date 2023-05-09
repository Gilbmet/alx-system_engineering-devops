#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """Recursively query the Reddit API and count the occurrences of given words in the titles of hot articles."""

    # Base case: no more articles to process
    if after == "STOP":
        # Sort and print the count dictionary
        sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_count:
            print("{}: {}".format(word, count))
        return

    # First call of the function: initialize count_dict
    if count_dict is None:
        count_dict = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "myBot/0.0.1"}

    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()

    articles = data.get("data", {}).get("children", [])

    # Update count_dict with the occurrences of the given words in the titles of the articles
    for article in articles:
        title = article.get("data", {}).get("title", "").lower()
        for word in word_list:
            if " {} ".format(word.lower()) in title:
                count_dict[word.lower()] += title.count(" {} ".format(word.lower()))

    # Recursive call with the name of the last article processed as the "after" parameter
    after = articles[-1].get("data", {}).get("name")
    count_words(subreddit, word_list, after=after, count_dict=count_dict)
