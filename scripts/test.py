import unittest, frontmatter, git

class TestKBFrontmatter(unittest.TestCase):

    
    def test_has_title(self):
        "Parse frontmatter and only the frontmatter"
        with open('tests/article_with_id.md') as f:
            metadata, content = frontmatter.parse(f.read())

        self.assertTrue('title' in metadata, "Article does not have an 'titl' in the frontmatter")

    def test_has_id(self):
        "Parse frontmatter and only the frontmatter"
        with open('tests/article_with_id.md') as f:
            metadata, content = frontmatter.parse(f.read())

        self.assertTrue('id' in metadata, "Article does not have an 'id' in the frontmatter")

    def test_has_locale(self):
        "Parse frontmatter and only the frontmatter"
        with open('tests/article_with_id.md') as f:
            metadata, content = frontmatter.parse(f.read())

        self.assertTrue('locale' in metadata, "Article does not have an 'locale' in the frontmatter")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKBFrontmatter)
    unittest.TextTestRunner(verbosity=2).run(suite)
