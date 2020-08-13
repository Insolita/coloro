#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:author Insolita https://twitter.com/DonnaInsolita
:url  https://github.com/insolita/coloro
:description Highlight hex colors in terminal
"""

import argparse
import os
import clipboard
import sys
import re


def hex_to_rgb(value):
    value = value.lstrip('#')
    if len(value) == 3:
        value += value
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def colorize(text):
    pattern = re.compile(r'#(?:[0-9a-fA-F]{3}){1,2}')
    matches = set(re.findall(pattern, text))
    for color in matches:
        (r, g, b) = hex_to_rgb(color)
        term_color = '\033[{};2;{};{};{}m {} \033[0m'.format(48, r, g, b, color)
        text = text.replace(color, term_color)
    print(text)


def main():
    text = None
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, nargs='?',
                        action="store", default=None, help="Text for colorize")
    parser.add_argument("-c", '--clip', action="store_true",
                        help="Process text from clipboard")
    args = parser.parse_args()
    if args.clip:
        try:
            text = clipboard.paste()
        except Exception:
            print('Sorry, seems clipboard is not supported')
            print('Try to install xsel or xclip')
            exit(1)
    elif args.text and os.path.isfile(args.text):
        with open(args.text) as f:
            text = f.read()
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(args.text):
        text = args.text
    else:
        print('text not matched')
        exit(0)

    colorize(text)
    exit(0)


if __name__ == '__main__':
    main()

