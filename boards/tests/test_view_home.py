from django.test import TestCase
from django.urls import resolve, reverse
from ..models import Board
from ..views import BoardListView

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        # This is a very simple test case. We are testing
        # the status code of the response. The status code
        # 200 means success
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        # Django uses the resolve function to match a requested
        # URL with a list of URLs listed in the urls.py module.
        # This test will make sure the URL /, which is the root
        # URL, is returning the home view.
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        # test if the response body contains a given text
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))