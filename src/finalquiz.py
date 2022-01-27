import json
from library.company import Employee,CompanyHelper




if __name__=="__main__":

    empsJson,emps = [],[]
    with open ("employee.json") as f:
        fcontent = f.read()
        empsJson = json.loads(fcontent)
        emps = [Employee(**empJ) for empJ in empsJson]
    ch = CompanyHelper(emps)
    print("-----Company Hierarchy-----")
    ch.print_company_hierarchy()
    
    print("-----Total Salary-----")
    print(ch.totalSalary)

    print("-----Employees Alphabetically-----")
    print(sorted(ch.employees.values()))

    
    try:
        print("-----Employees Validation-----")
        Employee(**{
            "id": 1000,
            "first_name": "Eric",
            "manager": 2,
            "salary": -1
        })
    except ValueError as ve:
        print(ve)
