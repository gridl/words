import sys
import shutil

from word_analysis.output import make_ouput
from word_analysis.copy import copy_repository
from word_analysis.analysis import get_top_words


def main(url, part_of_speech='ALL', object_type='ALL', output_method='console',
         tmp_dir='tmp'):
    parts_of_speech = ['VERB', 'NOUN', 'ADJ', 'ALL']
    objects_types = ['function', 'variable', 'ALL']
    output_methods = ['concole', 'json', 'csv']
    assert part_of_speech in parts_of_speech
    assert object_type in objects_types
    assert output_method in output_methods
    tmp_repo = copy_repository(url, tmp_dir)

    top_words = get_top_words(tmp_repo, part_of_speech, object_type)
    make_ouput(top_words, output_method)

    shutil.rmtree(tmp_repo)

if __name__ == "__main__":
    args = [arg for arg in sys.argv if arg != sys.argv[0]]
    main(*args)
