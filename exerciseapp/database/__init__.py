from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

# To destroy postgres database on heroku:
# heroku pg:reset DATABASE_URL --app=exercisingapp