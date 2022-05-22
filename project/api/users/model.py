import contextlib
import enum, os, uuid, json

class Branch(enum.Enum):
	CSE = 1
	EE = 2
	ME = 3

from project.extensions import db
from project.lib.model_utils  import ResourceMixin

basedir = os.path.abspath(os.path.dirname(__file__))

class User(ResourceMixin, db.Model):

	__tablename__ = "users"

	user_id = db.Column(db.String, unique=True, nullable=False, primary_key=True, index=True, default=uuid.uuid4)

	roll = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(120), nullable=False)
	email_id = db.Column(db.String(120), unique=True, nullable=False)
	google_id = db.Column(db.Unicode, index=True)
	branch = db.Column(db.String(120), nullable=False)
	image_url = db.Column(db.String(120))

def populate_users(app):
	with app.app_context():
		try:
			num_rows_deleted = db.session.query(User).delete()
			db.session.commit()
		except Exception:
			db.session.rollback()
		input_file = os.path.join(basedir, 'data.json')
		data = json.load(open(input_file))
		for user in data:
			new_user = User(
				user_id=user['user_id'],
				name=user['name'],
				roll=user['roll'],
				email_id=user['email_id'],
				google_id=user['google_id'],
				branch=user['branch'],
				image_url=user['image_url']
			)
			with contextlib.suppress(Exception):
				db.session.add(new_user)
		db.session.commit()