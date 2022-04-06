from spacy import training

nlp = Language.from_config(config)
nlp.initializa(get_examples)
nlp.update(examples)
nlp.to_disk(path)