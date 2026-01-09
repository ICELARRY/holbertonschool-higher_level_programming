#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            for post in response.json():
                print(post["title"])
    except requests.RequestException as e:
        print(f"Error: {e}")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed, Status Code: {response.status_code}")
            return False
        posts = [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in response.json()]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id","title","body"])
            writer.writeheader()
            writer.writerows(posts)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
