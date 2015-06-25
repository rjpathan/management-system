from openerp.osv import osv, fields

class task(osv.Model):
	_inherit = "project.task"

	_columns = {
		'audit_id': fields.many2one('mgmtsystem.audit', 'Audit'),
	}
