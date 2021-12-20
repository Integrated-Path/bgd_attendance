# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from odoo.exceptions import UserError

class HrAttendance(models.Model):
    _inherit = 'user.attendance'

    def data_format(self):
        result = []
        for line in self.sorted(reverse=False, key=lambda x: x.timestamp):
            if line.attendance_state_id.type == 'checkin':
                new_line = {
                    'check-in': line,
                    'check-out': None,
                    'employee': line.employee_id,
                    'check-in-date': line.timestamp + datetime.timedelta(hours=3),
                    'check-out-date': None,
                    'work-time': None
                    }
                result.append(new_line)
            elif line.attendance_state_id.type == 'checkout':
                employee_data = filter(lambda x: x['employee'] == line.employee_id, result)
                list_employee_data = list(employee_data)
                if len(list_employee_data) > 0 and not list_employee_data[-1]['work-time']:
                    check_in_line = list_employee_data[-1]
                    check_in_line['check-out'] = line
                    check_in_line['check-out-date'] = line.timestamp + datetime.timedelta(hours=3)
                    check_in_line['work-time'] = check_in_line['check-out-date'] - check_in_line['check-in-date']
                else:
                    continue

        # result = list( filter(lambda x: x['check-out'], result) )
        return result
        # raise UserError(str(result))