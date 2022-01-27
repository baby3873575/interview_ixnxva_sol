import sys
sys.path.append('./src')
import pytest
import json
from finalquiz import Employee



@pytest.fixture
def employees_from_file():
    empsJson,emps = [],[]
    with open ("employee.json") as f:
        fcontent = f.read()
        empsJson = json.loads(fcontent)
        emps = [Employee(**empJ) for empJ in empsJson]
    return emps
