import hashlib
import os
import re
from collections import deque
from urllib.parse import urlencode, urlparse
import urllib.request

import requests
from bs4 import BeautifulSoup
from app.service.HyperLinkParser import HyperlinkParser


class Scrapper:

    # Function to get the hyperlinks from a URL
    def get_hyperlinks(self, url):
        # Try to open the URL and read the HTML
        try:
            # Open the URL and read the HTM
            user_agent = 'Mozilla/6.0'
            headers = {'User-Agent': user_agent}
            request = urllib.request.Request(url=url, headers=headers)
            with urllib.request.urlopen(request) as response:
                # If the response is not HTML, return an empty list
                if not response.info().get('Content-Type').startswith("text/html"):
                    return []

                # Decode the HTML
                html = response.read().decode('utf-8')
        except Exception as e:
            print(e)
            return []

        # Create the HTML Parser and then Parse the HTML to get hyperlinks
        parser = HyperlinkParser()
        parser.feed(html)
        return parser.hyperlinks

    # Function to get the hyperlinks from a URL that are within the same domain
    def get_domain_hyperlinks(self, local_domain, url, http_url_pattern):
        clean_links = []
        for link in set(self.get_hyperlinks(url)):
            clean_link = None

            # If the link is a URL, check if it is within the same domain
            if re.search(http_url_pattern, link):
                continue
                # Parse the URL and check if the domain is the same
                url_obj = urlparse(link)
                if url_obj.netloc == local_domain:
                    clean_link = link

            # If the link is not a URL, check if it is a relative link
            else:
                if link.startswith("/"):
                    link = link[1:]
                elif (
                        link.startswith("#")
                        or link.startswith("mailto:")
                        or link.startswith("tel:")
                ):
                    continue
                clean_link = "https://" + local_domain + "/" + link

            if clean_link is not None:
                if clean_link.endswith("/"):
                    clean_link = clean_link[:-1]
                clean_links.append(clean_link)

        # Return the list of hyperlinks that are within the same domain
        return list(set(clean_links))

    def crawl(self, url, http_url_pattern):
        # Parse the URL and get the domain
        u = urlparse(url)
        p = str(u.path).split("/")[:-1]
        local_domain = u.netloc + "/".join(p)
        print(local_domain)
        # Create a queue to store the URLs to crawl
        queue = deque([url])

        # Create a set to store the URLs that have already been seen (no duplicates)
        seen = {url}

        filename_map = {}

        # Create a directory to store the text files
        if not os.path.exists("text/"):
            os.mkdir("text/")

        if not os.path.exists("text/" + local_domain + "/"):
            os.mkdir("text/" + local_domain + "/")

        # Create a directory to store the csv files
        if not os.path.exists("processed"):
            os.mkdir("processed")

        # While the queue is not empty, continue crawling
        while queue:

            # Get the next URL from the queue
            url = queue.pop()
            print(url)  # for debugging and to see the progress

            # Save text from the url to a <url>.txt file
            file_name = hashlib.sha256(url.encode()).hexdigest()
            filename_map[file_name] = file_name
            with open('text/' + local_domain + '/' + file_name + ".txt", "w", encoding="UTF-8") as f:
                user_agent = 'Mozilla/6.0'
                headers = {'User-Agent': user_agent}

                request = urllib.request.Request(url=url, headers=headers)
                req = urllib.request.urlopen(request)
                # Get the text from the URL using BeautifulSoup
                soup = BeautifulSoup(req.read(), "html.parser")

                # Get the text but remove the tags
                text = soup.get_text()

                # If the crawler gets to a page that requires JavaScript, it will stop the crawl
                if "You need to enable JavaScript to run this app." in text:
                    print("Unable to parse page " + url +
                          " due to JavaScript being required")

                # Otherwise, write the text to the file in the text directory
                f.write(text)
            print("GETT")
            # Get the hyperlinks from the URL and add them to the queue
            for link in self.get_domain_hyperlinks(local_domain, url, http_url_pattern):
                if link not in seen:
                    queue.append(link)
                    seen.add(link)
