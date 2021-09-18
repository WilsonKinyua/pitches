import unittest
from app.models import Post


class TestPost(unittest.TestCase):
    def setUp(self):
        self.new_post = Post(title="Test Post Title",
                             body="Test Content body", author_id="Test Post Author", slug="test-post-slug")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))
