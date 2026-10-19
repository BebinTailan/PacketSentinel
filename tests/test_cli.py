import contextlib
import io
import unittest

from packetsentinel import __version__
from packetsentinel.cli import main


class CliTests(unittest.TestCase):
    def test_version_flag_prints_version(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), self.assertRaises(SystemExit) as ctx:
            main(["--version"])
        self.assertEqual(ctx.exception.code, 0)
        self.assertIn(__version__, out.getvalue())

    def test_no_arguments_prints_help(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main([]), 0)
        self.assertIn("usage:", out.getvalue())


if __name__ == "__main__":
    unittest.main()
