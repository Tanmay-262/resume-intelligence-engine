SKILLS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pytorch",
    "docker",
    "aws",
    "react",
]
def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))