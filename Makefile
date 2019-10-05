app:
	python3 -m web_flask.app
apidev:
	HBNB_MYSQL_USER=app_dev HBNB_MYSQL_PWD=app_dev_pwd HBNB_MYSQL_DB=app_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_MYSQL_HOST=0.0.0.0 HBNB_API_PORT=5001 python3 -m api.app
setup_db:
	cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
new_user:
	HBNB_MYSQL_USER=app_dev HBNB_MYSQL_PWD=app_dev_pwd HBNB_MYSQL_DB=app_dev_db HBNB_TYPE_STORAGE=db HBNB_A\
PI_HOST=0.0.0.0 HBNB_MYSQL_HOST=0.0.0.0 HBNB_API_PORT=5001 ./test_user.py

server:
	ssh ubuntu@34.74.88.31 -i ~/.ssh/holberton
