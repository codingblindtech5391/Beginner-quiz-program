

def display_question(question):
    """ Display question and choices to user """

    print(question['question'])
    for option, text_in_question in question['options'].items():
        print(f"{option}: {text_in_question}\n")
    return None
