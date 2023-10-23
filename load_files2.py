import json
import os
import configparser
import concurrent.futures
import time
from queue import Queue
import subprocess
import gzip
import json
from compressed_json_wrapper import read_gzipped_json, GzippedJsonWriter
import re
from itertools import islice
from tqdm import tqdm
import threading

global giant_ass_list_to_download
giant_ass_list_to_download = []

def get_files(folder_path):
    """Gets all the JSON files in the specified folder and processes each one."""
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            data = read_json_file(file_path)
            # process_json(data)
            giant_ass_list_to_download.append(process_json(data))

    return giant_ass_list_to_download

def read_json_file(file_path):

    print(f"Read file: {file_path}")

    """Reads a JSON file and returns its content as a Python dictionary."""
    with open(file_path, 'r') as f:
        data = json.load(f)

    return data

def process_json(data):
    """Processes the JSON data according to the new format."""
    # Extract scrape settings
    scrape_settings = data['scrape_settings']
    subreddit = scrape_settings['subreddit']
    category = scrape_settings['category']
    n_results_or_keywords = scrape_settings['n_results_or_keywords']
    time_filter = scrape_settings['time_filter']

    print(f"Scrape Settings:")
    print(f"  Subreddit: {subreddit}")
    print(f"  Category: {category}")
    print(f"  Number of Results or Keywords: {n_results_or_keywords}")
    print(f"  Time Filter: {time_filter}")

    # Process each post in the data array
    for post in data['data']:
        author = post['author']
        created_utc = post['created_utc']
        distinguished = post.get('distinguished', None)
        edited = post['edited']
        post_id = post['id']
        is_original_content = post['is_original_content']
        is_self = post['is_self']
        link_flair_text = post.get('link_flair_text', None)
        locked = post['locked']
        name = post['name']
        nsfw = post['nsfw']
        num_comments = post['num_comments']
        permalink = post['permalink']
        score = post['score']
        selftext = post['selftext']
        spoiler = post['spoiler']
        stickied = post['stickied']
        title = post['title']
        upvote_ratio = post['upvote_ratio']
        url = post['url']

        print(f"\nPost Details:")
        print(f"  Author: {author}")
        print(f"  Created UTC: {created_utc}")
        print(f"  Distinguished: {distinguished}")
        print(f"  Edited: {edited}")
        print(f"  ID: {post_id}")
        print(f"  Is Original Content: {is_original_content}")
        print(f"  Is Self: {is_self}")
        print(f"  Link Flair Text: {link_flair_text}")
        print(f"  Locked: {locked}")
        print(f"  Name: {name}")
        print(f"  NSFW: {nsfw}")
        print(f"  Number of Comments: {num_comments}")
        print(f"  Permalink: {permalink}")
        print(f"  Score: {score}")
        print(f"  Self Text: {selftext}")
        print(f"  Spoiler: {spoiler}")
        print(f"  Stickied: {stickied}")
        print(f"  Title: {title}")
        print(f"  Upvote Ratio: {upvote_ratio}")
        print(f"  URL: {url}")

        # TODO: only add values over a certain threshold

        entry_json_to_download = {
          "author" : post['author'],
        #   "domain ": post['domain'],
          "post_id" : post['id'],
          "permalink" : post['permalink'],
          "subreddit_name" : subreddit,
          "url": post['url']
        }

        giant_ass_list_to_download.append(entry_json_to_download)

    return giant_ass_list_to_download

if __name__ == '__main__':
    # Replace with the path to your JSON file
    file_path = 'C:\git\RedditScrape\json\LegalTeens-top-100000-results.json'

    # Read and process the JSON file
    data = get_files(file_path)
    process_json(data)