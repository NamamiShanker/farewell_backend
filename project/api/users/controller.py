import os
from typing import Any, Dict
from flask import redirect, Blueprint, request, jsonify
from flask.views import MethodView

from .service import get_users_by_branch, get_user_by_id

from project.lib.errors import BadRequest, BaseError

user_blueprint = Blueprint("user", __name__)

class UserList(MethodView):

	@staticmethod
	def get(branch: str):
		if branch is None:
			raise BadRequest("branch is required", status=400)
		users = get_users_by_branch(branch)
		return jsonify(users)

class UserView(MethodView):

	@staticmethod
	def get(user_id: str):
		user = get_user_by_id(user_id)
		if user is None:
			raise BaseError("User not found", 404)
		print("Here")
		return jsonify(user)

user_blueprint.add_url_rule(
	"/users/<branch>",
	view_func=UserList.as_view("user_list"),
	methods=["GET"]
)