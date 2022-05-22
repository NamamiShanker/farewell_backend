import os

class BaseConfig:

	DEBUG=False
	TESTING=False
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	FRONTEND_APP_URL=os.environ.get("FRONTEND_APP_URL")