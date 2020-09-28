from hr import PayrollSystem
from productivity import ProductivitySystem
from employees import EmployeeDataBase

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDataBase()

employees = employee_database.employees()
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)


# import hr
# import employees
# import productivity
# import contacts

# manager = employees.Manager(1, 'Jose Contreras', 1500)
# manager.address = contacts.Address(
#     '121 Admin Road',
#     'Concord',
#     'NH',
#     '03301'
# )

# secretary = employees.Secretary(1, 'Laura Vergara', 750)
# secretary.address = contacts.Address(
#     '121 Admin Road',
#     'Concord',
#     'NH',
#     '03301'
# )


# sales_guy = employees.SalesPerson(3, 'Pablo Espinoza', 1000, 250)
# factory_worker = employees.FactoryWorker(4, 'Gustavo Cumare', 40, 20)
# temporary_secretary = employees.TemporarySecretary(5,'Fabiola Barrueta', 40, 9)

# # we comment this because Employee is an Abstract Class, so It can be instaciated
# # generic_employee = hr.Employee(4, 'Generic Employee')

# employees_list = [ manager, secretary, sales_guy, factory_worker, temporary_secretary ]


# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(employees_list, 40)

# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees_list)