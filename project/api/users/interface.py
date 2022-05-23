from dataclasses import dataclass

from .model import User as UserDB

@dataclass
class User:
	user_id: str
	roll: int
	name: str
	email_id: str
	google_id: str
	branch: str
	image_url: str

	@classmethod
	def instance_creator(cls, user_db: UserDB):
		return cls(
			user_id=user_db.user_id,
			roll=user_db.roll,
			name=user_db.name,
			email_id=user_db.email_id,
			google_id=user_db.google_id,
			branch=user_db.branch,
			image_url=user_db.image_url
		)

	@classmethod
	def get_all(cls):
		return [cls.instance_creator(user_db) for user_db in UserDB.query.all()]

	@classmethod
	def get_by_branch(cls, branch: str):
		return [
		    cls.instance_creator(user_db)
		    for user_db in UserDB.get_all({"branch": branch})
		]

	@classmethod
	def get_by_id(cls, user_id: str):
		user_db = UserDB.get_first({"user_id": user_id})
		if user_db is None:
			return None
		return cls.instance_creator(user_db)

	@classmethod
	def get_by_email_id(cls, email_id: str):
		user_db = UserDB.get_first({"email_id": email_id})
		if user_db is None:
			return None
		return cls.instance_creator(user_db)

	def register_google_id(self, google_id: str) -> None:
		user_db: UserDB = UserDB.get_first({"user_id": self.user_id})
		if(user_db):
			user_db.google_id = google_id
			user_db.update()