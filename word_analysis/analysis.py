import os
import ast
import collections
from nltk import pos_tag


def is_function(node):
    return isinstance(node, ast.FunctionDef)


def is_variable(node):
    return isinstance(node, ast.Name)


def get_name(node, object_type):
    if object_type == 'function' and is_function(node):
        name = node.name.lower()
    elif object_type == 'variable' and is_variable(node):
        name = node.id.lower()
    else:
        if is_function(node):
            name = node.name.lower()
        elif is_variable(node):
            name = node.id.lower()
        else:
            name = ''
    if name.startswith('__') or name.endswith('__'):
        name = ''
    return name


def get_all_names(tree, object_type):
    all_names = []
    for node in ast.walk(tree):
        name = get_name(node, object_type)
        if name:
            all_names.append(name)
    return all_names


def get_words_from_object_name(object_name, part):
    words = [word for word in object_name.split('_') if word]
    tagged_words = pos_tag(words, tagset='universal')
    valid_words = []
    if part != 'ALL':
        for word, tag in tagged_words:
            if tag == part:
                valid_words.append((word, tag))
    else:
        valid_words = tagged_words
    return valid_words


def get_objects(tree, object_type):
    objects_names = get_all_names(tree, object_type)
    return objects_names


def get_trees(path):
    trees = []
    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith('.py'):
                filename = os.path.join(dirname, file)
                with open(filename, 'r', encoding='utf-8') as attempt_handler:
                    main_file_content = attempt_handler.read()
                try:
                    tree = ast.parse(main_file_content)
                except SyntaxError as e:
                    print(e)
                else:
                    trees.append(tree)
    return trees


def get_words(trees, part_of_speech, object_type):
    words = []
    for t in trees:
        for object_name in get_objects(t, object_type):
            words += get_words_from_object_name(object_name, part_of_speech)
    return words


def get_top(words):
    top_verbs = collections.Counter(words).most_common()
    return top_verbs


def get_top_words(path, part_of_speech, object_type):
    trees = get_trees(path)
    words = get_words(trees, part_of_speech, object_type)
    top = get_top(words)
    return top
