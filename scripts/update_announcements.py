import os
import re
import unidecode

import pandas as pd
import requests

# Constants
ANNOUNCEMENTS_PATH = "../collections/announcements"
DATE_FORMAT = "%Y-%m-%d"

COURSE_ID = 21036

THREAD_URL = "https://edstem.org/us/courses/{course_id}/discussion/{thread_id}"
THREADS_API = f"https://us.edstem.org/api/courses/{COURSE_ID}/threads"

LIMIT = 30

SECRETS_DIR = os.path.join(os.path.expanduser("~"), ".secrets")
TOKEN_FILE = os.path.join(SECRETS_DIR, "ed_token")


def slugify(text):
    text = unidecode.unidecode(text).lower().strip()
    return re.sub(r"[\W_]+", "-", text).strip("-")  # Remove trailing or leading -


def get_token():
    if not os.path.isfile(TOKEN_FILE):
        token = input("Enter a Ed Token (ask Hunter if you don't know how): ")
        os.makedirs(SECRETS_DIR, exist_ok=True)
        with open(TOKEN_FILE, "w") as f:
            f.write(token)

    with open(TOKEN_FILE, "r") as f:
        return f.read().strip(" \n\t")


def parse_announcement_url(path):
    key = "ed_url"
    with open(path) as f:
        for line in f.readlines():
            if line.startswith(key):
                return line.split(":", maxsplit=1)[1].strip()

    raise ValueError(f"No EdStem URL {path}")


def get_website_announcements():
    urls = set()
    for announcement_file in os.listdir(ANNOUNCEMENTS_PATH):
        path = os.path.join(ANNOUNCEMENTS_PATH, announcement_file)
        url = parse_announcement_url(path)
        urls.add(url)
    return urls


def parse_date(timestamp):
    datetime = pd.to_datetime(timestamp)
    return datetime.tz_convert("America/Los_Angeles")


def get_ed_announcements(token):
    def request_threads(offset):
        r = requests.get(
            THREADS_API,
            params={
                "limit": LIMIT,
                "offset": offset,
                "sort": "date",
                "order": "asc",
                "filter": "staff",
            },
            headers={"x-token": token},
        )
        return r.json()["threads"]

    num_requests = 0
    threads = True

    while threads:
        threads = request_threads(LIMIT * num_requests)

        if threads:
            for thread in threads:
                if thread["type"] == "announcement":
                    yield thread

            num_requests += 1


def save_website_announcement(num, announcement, date):
    fname = slugify(announcement["title"])
    path = os.path.join(ANNOUNCEMENTS_PATH, f"{num:02}-{fname}.md")

    with open(path, "w") as f:
        f.write("---\n")
        f.write(f'title: "{announcement["title"]}"\n')
        f.write(f"date: {date.strftime(DATE_FORMAT)}\n")
        f.write(f'ed_url: {announcement["url"]}\n')
        f.write("---\n")
        f.write("\n")
        f.write("TODO\n")


def main():
    token = get_token()

    website_announcements = get_website_announcements()

    edstem_announcements = sorted(
        list(get_ed_announcements(token)), key=lambda a: parse_date(a["created_at"])
    )

    for announcement in edstem_announcements:
        announcement["url"] = THREAD_URL.format(
            course_id=COURSE_ID, thread_id=announcement["id"]
        )

        if announcement["url"] not in website_announcements:
            num = len(website_announcements)
            date = parse_date(announcement["created_at"])

            save_website_announcement(num, announcement, date)

            website_announcements.add(announcement["url"])


if __name__ == "__main__":
    main()
