JWT_SECRET_KEY = "913825f9b1415336f5ea4f5b92d44e2b6f2a6c8590b2d6c02cf680fde4be82d4"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 60 * 24  * 5

TOKEN_DESCRIPTION =  "It checks username and password if they are true, it returns JWT token to you."
TOKEN_SUMMARY = "It returns JWT token."

ISBN_DESCRIPTION = "It is a unique identifier for books"

DB_HOST = "localhost"
DB_USER = "admin"
DB_PASSWORD = "admin"
DB_NAME = "bookstore"
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
