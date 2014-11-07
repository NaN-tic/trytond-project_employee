# This file is part project_employee module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .work import *

def register():
    Pool.register(
        WorkEmployee,
        Work,
        module='project_employee', type_='model')
