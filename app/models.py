from django.db import models


def createAnswers(amount):
    return [
        {
            'id': answer_id,
            'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.' * answer_id,
            'like_number': answer_id,
            'correct': answer_id % 2 if True else False,
        } for answer_id in range(amount)
    ]


QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.' * question_id,
        'like_number': question_id,
        'answers_number': question_id,
        'tags': (f'tag #{i+1}' for i in range(question_id)),
        'answers': createAnswers(question_id)
    } for question_id in range(10)
]


OPTIONS = {
    'username': 'Cat',
    'password': 'password',
    'nickname': 'Bird',
    'is_auth': True
}


TAGS = [
    {
        'name': "Ta"+"g"*tag_id
    } for tag_id in range(10)
]