# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_resume():
    return {
        'title': fake.sentence(nb_words=6),
        'company': fake.sentence(nb_words=2),
        'job':fake.sentence(nb_words=1),
        'hability': fake.sentence(nb_words=35),
        'description': fake.sentence(nb_words=50),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'long_text': fake.text(3000),
        'middle_text': fake.text(1000),
        'date': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/cook,internet' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_resume())