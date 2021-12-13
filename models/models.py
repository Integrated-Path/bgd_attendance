# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from odoo.exceptions import UserError

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    def convert_time(self):
        x = datetime.datetime.strptime(self.check_in, "%m/%j/%y %H:%M").time()
        # raise UserError(self.check_in)
        return x
        