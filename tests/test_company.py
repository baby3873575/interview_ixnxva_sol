import sys
sys.path.append('./src')
import pytest
from finalquiz import CompanyHelper
import functools,operator,collections

def test_total_salary(employees_from_file):
    ch = CompanyHelper(employees_from_file)
    total = 0
    for emp in employees_from_file:
        total+=emp.salary
    assert ch.totalSalary==total


def test_sort_by_alphabetically(employees_from_file):
    ch = CompanyHelper(employees_from_file)
    empNames = []
    for emp in employees_from_file:
        empNames.append(emp.first_name)
    print(sorted(empNames))
    print(sorted(ch.employees.values()))
    assert [str(emp) for emp in sorted(ch.employees.values()) ]==sorted(empNames)