from settings import DB_NAME, DB_USER, DB_PASSWORD

database_path = "postgresql://{}:{}@localhost:5432/{}".format(DB_USER, DB_PASSWORD, DB_NAME)