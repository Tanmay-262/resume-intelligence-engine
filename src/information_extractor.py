import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_email(text):
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    match = re.search(pattern, text)

    return match.group() if match else None


def extract_phone(text):
    pattern = r"\+?\d[\d\s\-]{8,15}"

    match = re.search(pattern, text)

    return match.group() if match else None


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return "Not Found"