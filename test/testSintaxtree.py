from unittest import TestCase

import homology.sintaxtree as st

class TestBasicSnippet(TestCase):
    def setUp(self):
        self.snippet = st.CompositeSnippet(st.SimpleSnippet('if'), '$', st.SimpleSnippet('i==1'))

    def test_repr(self):
        self.assertEqual(str(self.snippet),'if$i==1')