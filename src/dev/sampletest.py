from unittest import TestCase

import basic_example as auth

class StandAloneTests(TestCase):
    """Test the stand-alone module functions."""


    def test_login(self):
        """Test the login function."""
        self.assertEqual(auth.authentication('Pavan', 'Tirumalasetti'),"Correct")