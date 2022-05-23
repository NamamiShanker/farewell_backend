import os
from typing import Any, Dict
from flask import redirect, Blueprint, request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError

from .service import get_users_by_branch, get_user_by_id, get_all_users, register_google_id
from .schema import user_register_schema

from project.lib.errors import BadRequest, BaseError, ServerError

user_blueprint = Blueprint("user", __name__)

class UserList(MethodView):

	@staticmethod
	def get():
		return jsonify(get_all_users())

	@staticmethod
	def put():
		if val := user_register_schema.validate(request.json):
			raise BadRequest(val, status=400)
		try:
			user_info = user_register_schema.load(request.get_json())
			register_google_id(user_info["email_id"], user_info["google_id"])
			resp = {"message": "User registered successfully"}
		except ValidationError as err:
			raise BadRequest(message=str(err), status=422) from err
		except BadRequest as err:
			raise BadRequest(message=err.message, status=err.status) from err
		except Exception as e:
			raise ServerError(message=str(e), status=500) from e
		else:
			return resp, 201

class UserBranchList(MethodView):

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
	view_func=UserBranchList.as_view("user_branch_list"),
	methods=["GET"]
)

user_blueprint.add_url_rule(
	"/users/<user_id>",
	view_func=UserView.as_view("user_view"),
	methods=["GET"]
)

user_blueprint.add_url_rule(
	"/users",
	view_func=UserList.as_view("user_list"),
	methods=["GET", "PUT"]
)