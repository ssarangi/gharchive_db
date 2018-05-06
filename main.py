from crawler import Crawler
import argparse

def main():
    crawler = Crawler()
    repos = crawler.fetch_repositories_with_stars_greater_than(100000)
    print(repos)

if __name__ == "__main__":
    main()