from flask import Flask

def register_blueprint(app: Flask):

	from project.api.users import user_blueprint
	app.register_blueprint(user_blueprint, url_prefix="/api")