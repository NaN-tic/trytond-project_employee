#This file is part project_employee module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Work', 'WorkEmployee']
__metaclass__ = PoolMeta


class WorkEmployee(ModelSQL):
    'Project Work - Employee'
    __name__ = 'project.work-company.employee'
    _table = 'project_work_company_employee_rel'
    work = fields.Many2One('project.work', 'Work', ondelete='CASCADE',
        select=True, required=True)
    employee = fields.Many2One('company.employee', 'Employee',
        ondelete='CASCADE', select=True, required=True)


class Work:
    __name__ = 'project.work'
    employees = fields.Many2Many('project.work-company.employee', 'work',
        'employee', 'Employees')
    employee = fields.Many2One('company.employee', 'Current Employee',
        domain=[
            ('company', '=', Eval('company')),
            ('id', 'in', Eval('employees', [])),
            ],
        depends=['employees', 'company'])
