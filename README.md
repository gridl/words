# Words analyzer
## installation:
```
git clone https://github.com/SirNicolas/words.git
```
## run & params:
* url - your Github project url like 'https://github.com/SirNicolas/words.git' (required param)
* part_of_speech - VERB, NOUN, ADJ or ALL (default ALL)
* objects_types - function, variable or ALL (default ALL)
* output_methods - console, json or csv (default to console)
* tmp_dir - temporary directory for cloned repo f your project (default to /tmp)
```
python main.py url
```
or
```
python main.py url part_of_speech object_type output_method
```
