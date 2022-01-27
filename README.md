# ixnxva sol


#### code location:

src/finalquiz.py
Is the main script to run the quiz program
To run the program:

```
python src/finalquiz.py 
```

src/library/company.py
Contains the class definition of a company and the core logic that manipulate hierarchy. There are three classes: Employee, Department, Companyhelper.

##### Employee
1. The employee class extends pydantic model that can helps to do a basic validation on the input.
2. It has \__lt__ method that implement it's comparator which be use with sorted() function
3. It has \__repr__ method so when trying to print a object in a dictionary(in CompanyHelper), it can shows first_name field
4. In order to prevent Employee been created and init multiple time to reduce the risk of duplication, the \__init__ and \__new__ method has use class variable to prevent the reinitialization.

##### Department
1. Is a storage for grouping manager with it's member while holding the child departments so we can make traverse easilier.

##### CompanyHelper
1. A class that can manipulating Employee and Department from a high level perspective.  
2. It managed to build the department map and it's hierarchy after all employees are added.


### Unit test with pytest
#### code location:
```
tests/test_*.py
pytest tests/test_*.py
```
