
import pytest
from finalquiz import Employee

@pytest.mark.parametrize(
    "kwarg",
    [
        {
            "id": 1,
            "first_name": "Dave",
            "manager": 2,
            "salary": 100000
        },
        {
            "id": 2,
            "first_name": "Jeff",
            "manager": None,
            "salary": 110000
        },
    ]
)
def test_employee_validation(kwarg):
    Employee(**kwarg)



@pytest.mark.parametrize(
    "kwarg",
    [
        {
            "id": "string",
            "first_name": "Dave",
            "manager": 2,
            "salary": 100000
        },
        {
            "id": 2,
            "first_name": "Dave",
            "manager": None,
            "salary": -1
        },
    ]
)
def test_employee_validation_error(kwarg):
    with pytest.raises(ValueError):
        Employee(**kwarg)

def test_employee_singleton():
    Dave = Employee(**{
            "id": 1,
            "first_name": "Dave",
            "manager": 2,
            "salary": 100000
    })

    Dave2 = Employee(**{
            "id": 1,
            "first_name": "Dave",
            "manager": 2,
            "salary": 100000
    })
    assert Dave2==Dave
    assert len(Dave)==1