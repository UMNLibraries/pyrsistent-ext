import sys 
import os
sys.path.append(os.path.relpath(".venv/src/pyrsistent/tests"))
#from record_test import ARecord
from record_test import *

import pytest
from pyrsistent import PRecord

def test_is_precord():
    assert issubclass(ARecord, PRecord)

def test_create_ignore_extra_true():
    raise Exception
