import re
import time

import requests
import execjs
import json
import csv

headers = {
    "authority": "www.xiaohongshu.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/json;charset=UTF-8",
    "referer": "https://www.xiaohongshu.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
}

# Initialize a session to handle cookies
session = requests.Session()


# Define a function to perform the keyword search and retrieve notes
def keyword_search(keyword):
    # API endpoint for searching notes
    search_url = "https://www.xiaohongshu.com/api/sns/v1/search/notes"

    # Parameters for the search request
    params = {
        "keyword": keyword,
        "page": 1,
        "pageSize": 20  # 20 notes per page
    }

    # Send the search request
    response = session.get(search_url, params=params, headers=headers)
    data = response.json()

    # Extract and process notes from the response
    if data.get("data") and data["data"].get("notes"):
        notes = data["data"]["notes"]
        for note in notes:
            # Process each note here
            note_id = note["id"]
            note_title = note["title"]
            print(f"Processing note: {note_title} (ID: {note_id})")

            # Optionally, you can call another function to crawl comments for each note
            crawl_comments(note_id)


# Define a function to crawl comments for a given note
def crawl_comments(note_id):
    # API endpoint for retrieving comments of a note
    comments_url = f"https://www.xiaohongshu.com/api/sns/v6/note/{note_id}/comments"

    # Send request to retrieve comments
    response = session.get(comments_url, headers=headers)
    data = response.json()

    # Process comments from the response
    if data.get("data") and data["data"].get("comments"):
        comments = data["data"]["comments"]
        for comment in comments:
            # Process each comment here
            comment_content = comment["content"]
            user_nickname = comment["user"]["nickname"]
            print(f"Comment by {user_nickname}: {comment_content}")

            # Optionally, you can save the comments to a file or database


# Define the main function
def main():
    keyword = '成都citywalk'  # Specify the keyword for search
    keyword_search(keyword)


# Entry point of the script
if __name__ == "__main__":
    main()