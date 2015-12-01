# This file is part of the project_employee module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProjectEmployeeTestCase(ModuleTestCase):
    'Test Project Employee module'
    module = 'project_employee'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProjectEmployeeTestCase))
    return suite