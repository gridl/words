import json
import csv


def to_console(words):
    for word in words:
        print(word)


def to_json(words):
    data = json.dumps(words)
    with open('words.json', 'w') as f:
        f.write(data)


def to_csv(words):
    with open('words.csv', 'wb') as out:
        csv_out = csv.writer(out)
        # csv_out.writerow(['name', 'num'])
        # for word in words:
        #     csv_out.writerow(word)
        csv_out.writerows(words)


def make_ouput(words, output_method):
    if output_method == 'console':
        to_console(words)
    elif output_method == 'json':
        to_json(words)
    elif output_method == 'csv':
        to_csv(words)
