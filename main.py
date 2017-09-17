import ast
import os
import collections

from nltk import pos_tag


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VBZ'


def get_trees(_path):
    filenames = []
    trees = []
    path = _path
    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
                if len(filenames) == 100:
                    break
    print('total %s files' % len(filenames))
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
        else:
            trees.append(tree)
    print('trees generated')
    return trees


def get_functions_names(tree):
    return [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]  # noqa


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_top_functions_names_in_path(path, top_size=10):
    trees = [t for t in get_trees(path) if t]
    verbs = []
    for t in trees:
        for node in get_functions_names(t):
            fnc_name = node.name.lower()
            if not (fnc_name.startswith('__') and fnc_name.endswith('__')):
                verbs += get_verbs_from_function_name(fnc_name)
    print('verbs from functions names extracted')
    top_verbs = collections.Counter(verbs).most_common(top_size)
    return top_verbs


wds = []
projects = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
]

for project in projects:
    path = os.path.join('.', project)
    wds += get_top_functions_names_in_path(path)

top_size = 200
print('total %s words, %s unique' % (len(wds), len(set(wds))))
for word, occurence in collections.Counter(wds).most_common(top_size):
    print(word, occurence)
