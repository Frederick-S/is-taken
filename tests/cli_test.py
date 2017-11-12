import io
import sys
import unittest
from contextlib import redirect_stdout
from istaken.main import main


class TestCli(unittest.TestCase):
    def test_if_package_name_is_taken(self):
        sys.argv[1:] = []
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertEqual('Usage: is-taken package-name\n', f.getvalue())

        sys.argv[1:] = ['flask']
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertEqual('flask is taken\n', f.getvalue())

        sys.argv[1:] = ['abc123xyz321']
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertTrue('abc123xyz321 is free to use\n', f.getvalue())


if __name__ == '__main__':
    unittest.main()
