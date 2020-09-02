from db import execute, fetch

sys.path.insert(0,'/home/gambo/Documents/API_Course/models')
from jwt_user import JWTUser


async def check_jwt_user(user:)
	query = """select * from users where username = :username and
										 password = :password"""

	values = {"username":user.username, "password": user.password}

	result = await fetch(query, True, values)
	if result is None:
		return False
	else:
		True