from marshmallow import Schema, fields

class UserRegisterSchema(Schema):
	"""
	User register schema
	"""
	email_id = fields.Email(required=True)
	google_id = fields.Str(required=True)

user_register_schema = UserRegisterSchema()