
from pydantic.dataclasses import dataclass
from pydantic import BaseModel,PrivateAttr,Extra,PositiveFloat
from typing import Optional,List
from common.singleton import Singleton

class Employee(BaseModel,extra=Extra.allow):
    __empRegistry = {}
    _initialized = False
    id: int
    first_name: str
    salary: PositiveFloat
    manager: Optional[int]
    
    def __new__(cls,*args,**kwargs):    
        if id := kwargs.get("id",None):
            if id not in Employee.__empRegistry:
                instance = super(Employee, cls).__new__(cls)
                Employee.__empRegistry[id]=instance
            return Employee.__empRegistry[id]
        else:
            raise ValueError("missing id field")
        
    def __init__(self,**data):
        if(self._initialized): return
        super().__init__(**data)
        self._initialized = True
        
    def __lt__(self,other) -> bool:
        return self.first_name < other.first_name 

    def __str__(self) -> str:
        return self.first_name
        
    def __repr__(self) -> str:
        return self.first_name

    @classmethod
    def __len__(cls)->int:
        return len(cls.__empRegistry)



class Department:
    name:str
    members: dict
    manager: Employee
    children:List['Department']
    
    def __init__(self,name:str,manager:Employee) -> None:
        self.name = name
        self.manager=manager
        self.members={}
        self.children={}
        
    def add_member(self,member:Employee)->None:
        self.members[member.id] = member

    def add_children(self,dept:'Department')->None:
        self.children[dept.name] = dept



class CompanyHelper(metaclass=Singleton):
    employees = {}
    departments = {}
    rootdept = None
    totalSalary = 0

    @staticmethod
    def get_department_name(emp:Employee):
        return emp.id

    def __init__(self,emps:List[Employee]) -> None:
        for emp in emps:
            self.add_employee(emp)

        self.build_company()
    
    
    def add_employee(self,emp:Employee)->None:
        self.employees[emp.id] = emp
        self.totalSalary += emp.salary



    def build_company(self)->None:
        self.build_dept()
        self.build_dept_hierarchy()

    def build_dept(self)->None:
        for id,emp in self.employees.items():
            if emp.manager is None: #hi boss
                self.rootdept = self.departments[CompanyHelper.get_department_name(emp)]
                continue
            empManager = self.employees[emp.manager]
            deptName = CompanyHelper.get_department_name(empManager)
            if deptName is None:
                self.departments[deptName] = Department(name=deptName, manager=self.employees[emp.manager])
            elif deptName not in self.departments:
                self.departments[deptName] = Department(name=deptName, manager=self.employees[emp.manager])
            self.departments[deptName].add_member(emp)

    def build_dept_hierarchy(self)->None:
        for _,dept in self.departments.items():
            # add children to parrent dept
            if dept == self.rootdept:
                continue
            deptManager = dept.manager
            deptName = CompanyHelper.get_department_name(self.employees[deptManager.manager])
            parentDept = self.departments[deptName]
            parentDept.add_children(dept)

    def print_company_hierarchy(self)->None:
        queue = [self.rootdept]
        queueNextLevel = []
        level = 0
        while True:
            dept = queue.pop(0)
            print("{indent}{people}".format(indent="  "*level,people=dept.manager.first_name))
            print("{indent}Employees of {people}".format(indent="  "*level,people=dept.manager.first_name))
            for _,emp in dept.members.items():
                print("{indent}{people}".format(indent="    "*level,people=emp.first_name))
            for _,childDept in dept.children.items():
                queueNextLevel.append(childDept)
            
            if len(queue)==0 and len(queueNextLevel)==0:
                break
            elif len(queue)==0:
                queue = queueNextLevel
                queueNextLevel = []
                level+=1
            else:
                assert False, "Unexpected execution"
