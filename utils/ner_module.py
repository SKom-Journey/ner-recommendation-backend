import spacy

def get_recommendation(text: str):
    nlp_ner = spacy.load("lib/restaurant_ner_recommendation")
    doc = nlp_ner(text)

    for ent in doc.ents:
        print(ent.text, ent.label_)
    return