from typing import List, Dict, Any
from .interface import User

def get_users_by_branch(branch: str) -> List[Dict[str, Any]]:
	return User.get_by_branch(branch)

def get_user_by_id(user_id: str) -> Dict[str, Any]:
	return User.get_by_id(user_id)