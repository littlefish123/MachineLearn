import spacy

nlp = spacy.load('en_core_web_trf')

# capital character is important to identify ORG
sentence = "Apple is looking at buying UK startup for $100 billion."

doc = nlp(sentence)

for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)