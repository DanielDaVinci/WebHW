from django.db import models

# Create your models here.

class question:
    def __init__(self, question_id, title, text, tags, answers):
        self.id = question_id
        self.title = title
        self.text = text
        self.tags = tags
        self.answers = answers
        pass

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.' * question_id,
        'answers_number': question_id*question_id,
        'tags': (f'tag #{i}' for i in range(question_id)),
        'answers': (f'{i}' for i in range(question_id))
    } for question_id in range(10)
]