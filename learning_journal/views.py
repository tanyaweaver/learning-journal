from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def lists(request):
    imported_text = open(os.path.join(HERE, 'templates/home_page.html')).read()
    return Response(imported_text)


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
    config.add_view(lists, route_name='lists')
    config.add_view(create, route_name='create')
    config.add_view(update, route_name='update')
    config.add_view(detail, route_name='detail')
