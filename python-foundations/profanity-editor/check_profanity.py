import urllib


def read_file():
    quotes = open("/Users/lbain/code/personal/udacity/python-foundations/profanity-editor/movie_quotes.txt")
    content = quotes.read()
    quotes.close()
    check_profanity(content)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if output == 'true':
        print('Profanity alert!')
    elif output == 'false':
        print('No curse words found')
    else:
        print('Error checking document')

read_file()
