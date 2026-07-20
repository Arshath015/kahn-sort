import pytest
import sys
from io import StringIO
from cli import main

def test_cli():
    sys.argv = ['cli.py', '--vertices', '6', '--edges', '5 2', '5 0', '4 0', '4 1', '2 3', '3 1']
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    main()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue().strip() == '5 4 2 3 1 0'