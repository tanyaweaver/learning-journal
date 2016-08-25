import pytest

from pyramid import testing


def test_detail():
    from learning_journal.views import detail
    request = testing.DummyRequest()
    info = detail(request)
    # import pdb; pdb.set_trace()
    assert 'title' in info['entries'][0]


@pytest.fixture()
def testapp():
    from learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'owner: Tatiana Weaver' in response.body


def test_root_contents(testapp):
    from learning_journal.views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll('article'))





# import unittest

# from pyramid import testing


# class ViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()

#     def tearDown(self):
#         testing.tearDown()

#     def test_my_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['project'], 'journal')


# class FunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from journal import main
#         app = main({})
#         from webtest import TestApp
#         self.testapp = TestApp(app)

#     def test_root(self):
#         res = self.testapp.get('/', status=200)
#         self.assertTrue(b'Pyramid' in res.body)
