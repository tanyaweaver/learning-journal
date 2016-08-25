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


@view_config(route_name='create', renderer='templates/new_entry.jinja2')
def create(request):
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='templates/single_entry.jinja2')
def detail(request):
    return {"entries": ENTRIES}


@view_config(route_name='update', renderer='templates/edit_entry.jinja2')
def update(request):
    return {"entries": ENTRIES}
