Blog : https://vijay-anandan.medium.com/custom-named-entity-recognition-ner-model-with-spacy-3-in-four-steps-7e903688d51

1. git clone https://github.com/Vijayvj1/Custom_NER_Spacy3.git
2. python -m pip install -r requirements.txt
3. python -m spacy info
    version 3.2.3
    python 3.6.8
    pipeline en_core_web_sm (3.2.0) 
4. mkdir corpus
5. python scripts/convert.py en assets/train.json corpus/train.spacy
6. python scripts/convert.py en assets/dev.json corpus/dev.spacy
7. mkdir configs   
8. python -m spacy init config --lang en --pipeline ner configs/config.cfg --force
9. mkdir training   
9. python -m spacy train configs/config.cfg --output training/ --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy --training.eval_frequency 10 --training.max_steps 100 --gpu-id -1


Explain
=======

<python -m spacy train config.cfg --paths.train ./train.spacy --paths.dev ./dev.spacy>

Dev --> Validation Data 

train --> Training Data 


Output
======

E — Epochs

optimization steps

LOSS NER — model loss

ENTS_F, ENTS_P, and ENTS_R — precision, recall and fscore of the model



10. mkdir images
11. python predict.py
check result under images/sentences.htm