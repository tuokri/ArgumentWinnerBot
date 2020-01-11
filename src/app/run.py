import argparse
import sys
from argparse import Namespace

import praw


def learn():
    pass


def scrape(reddit: praw.Reddit):
    pass


def run(reddit: praw.Reddit):
    pass


def parse_args() -> Namespace:
    ap = argparse.ArgumentParser()
    meg = ap.add_mutually_exclusive_group()
    meg.add_argument(
        "--scrape",
        action="store_true",
        default=False,
        help="scrape Reddit and build comment database",
    )
    meg.add_argument(
        "--learn",
        action="store_true",
        default=False,
        help="learn model from comment database",
    )
    meg.add_argument(
        "--run",
        action="store_true",
        default=False,
        help="run application, replying to Reddit comments based "
             "on the learned model",
    )
    return ap.parse_args()


def main():
    args = parse_args()

    if args.learn:
        learn()
    else:
        reddit = praw.Reddit()
        if args.run:
            run(reddit)
        elif args.scrape:
            scrape(reddit)
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
