import pytest

# from webtest import TestApp

from pyramid import testing

from learning_journal.views import ENTRIES, detail, create, lists

from pyramid.httpexceptions import HTTPNotFound

# import pdb; pdb.set_trace()

KEYS = ['title', 'date', 'id', 'body']

STRINGS = [
    b"Learning Journal",
    b"Code 401 - Software Development in Python",
    b"owner: Tatiana Weaver",
    b"Home",
    b"Code Fellows | Code 401 - Python"
]

ROUTES = ['/journal/new-entry', r'/journal/2/edit-entry']


@pytest.mark.parametrize('key', KEYS)
def test_detail_update(key):
    """
    Test that response for routes 'detail' and 'update'
    has <title>, <id>, <date>, <body>.
    """
    request = testing.DummyRequest()
    request.matchdict['id'] = 3
    info = detail(request)
    assert key in info['entry']


@pytest.mark.parametrize('key', KEYS)
def test_lists(key):
    """
    Test that response for 'lists' route (for home_page)
    has <title>, <id>, <date>, <body>.
    """
    request = testing.DummyRequest()
    info = lists(request)
    assert key in info['entries'][0]


def test_create():
    """
    Test that response for 'create' route
    is an empty dictionary
    """
    request = testing.DummyRequest()
    info = create(request)
    assert info == {}


def test_detail_not_found():
    """
    Tests whether request with a wrong id in url
    raises HTTPNotFound error.
    """
    with pytest.raises(HTTPNotFound):
        request = testing.DummyRequest()
        request.matchdict['id'] = 300
        info = detail(request)


@pytest.fixture()
def testapp():
    from learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


@pytest.mark.parametrize('b_string', STRINGS)
def test_layout_components(b_string, testapp):
    """Test whether the layout renders correctly."""
    response = testapp.get('/', status=200)
    assert b_string in response.body


def test_lists_contents(testapp):
    """Test whether number of <articles> on the home_page
    is equal to number of entries in ENTRIES in views.py."""
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll('article'))


@pytest.mark.parametrize('route', ROUTES)
def test_create_contents(route, testapp):
    """Test whether there are 2 <input> fields on the new_entry page."""
    response = testapp.get(route, status=200)
    print(response)
    html = response.html
    assert 2 == len(html.findAll('input'))
