from pyramid.response import Response
import os
from pyramid.view import view_config

HERE = os.path.dirname(__file__)


ENTRIES = [
     {
        "title": "Day1",
        "id": 1,
        "date": "August 21, 2016",
        "body": "Today I learned about <strong>Pyramid</strong>."
     },
     {
        "title": "Day2",
        "id": 2,
        "date": "August 22, 2016",
        "body": "Today I learned about heaps and templates."
     },
     {
        "title": "Day3",
        "id": 3,
        "date": "August 23, 2016",
        "body": "Today I learned about deploying to Heroku."
     },
     {
        "title": "Day4",
        "id": 4,
        "date": "August 25, 2016",
        "body": "Today I learned about deploying to birds."
     },
]


@view_config(route_name='lists', renderer='templates/home_page.jinja2')
def lists(request):
    return {"entries": ENTRIES}


def create(request):
    imported_text = open(os.path.join(HERE, 'templates/new_entry.html'))\
        .read()
    return Response(imported_text)


def detail(request):
    imported_text = open(os.path.join(HERE, 'templates/single_entry.html'))\
        .read()
    return Response(imported_text)


def update(request):
    imported_text = open(os.path.join(HERE, 'templates/edit_entry.html'))\
        .read()
    return Response(imported_text)


def includeme(config):
    # config.add_view(lists, route_name='lists')
    config.add_view(create, route_name='create')
    config.add_view(update, route_name='update')
    config.add_view(detail, route_name='detail')
