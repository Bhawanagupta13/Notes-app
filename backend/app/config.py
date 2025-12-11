import os
class settings:
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    mongo_db_name = os.getenv("MONGO_DB_NAME", "mydatabase")
    jwt_secret_key = os.getenv("JWT_SECRET", "dev_secret_key_change_in_prod")
    jwt_algorithm = "HS256"
    access_token_expires_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES", 60))
settings = settings()