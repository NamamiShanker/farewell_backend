from typing import List, Dict, Any
from .interface import User

def get_users_by_branch(branch: str) -> List[Dict[str, Any]]:
	return User.get_by_branch(branch)

def get_user_by_id(user_id: str) -> Dict[str, Any]:
	return User.get_by_id(user_id)

def get_all_users() -> List[Dict[str, Any]]:
	return User.get_all()

def register_google_id(user_email: str, google_id: str) -> None:
	user: User = User.get_by_email_id(user_email)
	user.register_google_id(google_id)