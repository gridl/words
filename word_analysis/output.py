import json
import csv


def to_console(words):
    for word in words:
        print(word)


def to_json(words):
    data = json.dumps(words)
    with open('words.json', 'w') as f:
        f.write(data)
    print('Imported into words.json')


def to_csv(words):
    with open('words.csv', 'w', newline='') as csvfile:
        csv_out = csv.writer(csvfile, delimiter=' ',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for word in words:
            csv_out.writerow(word)
    print('Imported into words.csv')


def make_ouput(words, output_method):
    if output_method == 'console':
        to_console(words)
    elif output_method == 'json':
        to_json(words)
    elif output_method == 'csv':
        to_csv(words)
