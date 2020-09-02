import sys
from datetime import datetime, timedelta
from utils.const import JWT_EXPIRATION_TIME_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM
from passlib.context import CryptContext
import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import time
from starlette.status import HTTP_401_UNAUTHORIZED

sys.path.insert(0,'/home/gambo/Documents/API_Course/models')
from jwt_user import JWTUser

oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"])



def get_hashed_password(password):
	return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
	try:
		return pwd_context.verify(plain_password, hashed_password)	
	except Exception as e:
		return False


# Authenticate username and password to give JWT token
def authenticate_user(user: JWTUser):
	hashed_password = get_hashed_password(user.password)
	user.password = hashed_password
	
	if fake_jwt_user1.username == user.username:
		if verify_password(user.password, fake_jwt_user1.password):
			user.role = "admin"
			return user

	return None


# Create access JWT token
def create_jwt_token(user:JWTUser):
	expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
	jwt_payload = {"sub":user.username,
					"role":user.role,
					"exp":expiration}
	jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

	return jwt_token


# Check whether JWT token is correct
def check_jwt_token(token: str = Depends(oauth_schema)):
	try:
		jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
		username = jwt_payload.get("sub")
		role = jwt_payload.get("role")
		expiration = jwt_payload.get("exp")

		if time.time() < expiration:
			if fake_jwt_user1.username == username:
				return final_checks(role)


	except Exception as e:
		
		return False

	
	raise False

# Last checking and returning the final result
def final_checks(role:str):
	if role == "admin":
		return True
	else:
		
		return False


