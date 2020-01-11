import argparse
import configparser
import sys
from argparse import Namespace
from pathlib import Path

import praw

CONFIG_PATH = Path("config.cfg")


def learn():
    pass


def scrape(reddit: praw.Reddit):
    pass


def run(reddit: praw.Reddit):
    pass


def read_config(config_path: Path) -> configparser.ConfigParser:
    config_path = str(config_path)
    cp = configparser.ConfigParser()
    found = cp.read(config_path, encoding="utf-8")
    if not found:
        raise RuntimeError(f"unable to locate config file: {config_path}")
    return cp


def find_config(config_path: Path) -> Path:
    config_path = Path(config_path)
    if config_path.exists():
        return config_path
    else:
        app_dir = Path(__file__)
        cfg_path = app_dir.parent / config_path
        if not cfg_path.exists():
            raise RuntimeError(f"unable to locate config file: {config_path}")
        else:
            return cfg_path


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
    config = read_config(find_config(CONFIG_PATH))
    reddit_config = config["reddit"]

    if args.learn:
        learn()
    else:
        reddit = praw.Reddit(**reddit_config)
        if args.run:
            run(reddit)
        elif args.scrape:
            scrape(reddit)
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
