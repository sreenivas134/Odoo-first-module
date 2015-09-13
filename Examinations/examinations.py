from openerp.osv import fields, osv

class Examinations(osv.osv):
    _name='examinations.custom'

    _columns = {
        'name' : fields.char('Examination',required=True),
        'subject' : fields.char('Subject', required=True),
        'exam_date' : fields.datetime('Date and Time of Date'),
        'exam_hall' : fields.char('Examination Hall'),
        'max_marks' : fields.integer('Maximum Marks'),
    }
    