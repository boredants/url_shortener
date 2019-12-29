# Requires python > 3.7
# pip3 install bitlyshortener
# Requires a bitly account and oauth key

import sys
import os.path
from bitlyshortener import Shortener
token = ['<YOUR TOKEN HERE>']
shortener = Shortener(tokens=token, max_cache_size=8192)
urlDict = {}


def shorten_single_url():
    url = input('\nEnter a url to shorten: ')
    urlDict[url] = shortener._shorten_url(url)
    
    for key in urlDict:
        print("\n{} : {}".format(key, urlDict[key]))

    to_file()


def shorten_url_list():
    urls = input('\nEnter a text file of urls to shorten: ')
    print()
    if os.path.isfile(urls):
        with open(urls, 'r') as f:
            for line in (f.readlines()):
                urlDict[line] = shortener._shorten_url(line)
            for key in urlDict:
                print("{} : {}".format(key.strip(), urlDict[key]))

    to_file()


def to_file():
    answer = input('\nWrite output to a file (Y|N)? ')
    if answer.lower() == 'y':
        write_to_file()
    elif answer.lower() == 'n':
        print('\nDone.  Exiting...')
        sys.exit()
    else:
        print('\nInvalid response.  Exiting...')
        sys.exit()


def write_to_file():
    outFile = input('\nEnter a file name: ')
    with open(outFile, 'w') as f:
        for key in urlDict:
            print("{} : {}".format(key.strip(), urlDict[key]), file=f)

    print('\nResults written to {}.  Exiting...\n'.format(outFile))


def main():
    print('\n*****************')
    print('* URL SHORTENER *')
    print('*****************\n')
    choice = input('Shorten a (S)ingle file or a (L)ist of files? ')
    if choice.lower() == 's':
        shorten_single_url()
    elif choice.lower() == 'l':
        shorten_url_list()
    else:
        print('\nCorrect responses are either S or L.  Exiting...\n')
        sys.exit()


if __name__ == '__main__':
    main()
