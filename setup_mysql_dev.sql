-- prepares a MySQL server for the project:
-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on the database hbnb_dev_db
-- hbnb_dev should have SELECT privilege on the database performance_schema
CREATE DATABASE IF NOT EXISTS app_dev_db;
CREATE USER IF NOT EXISTS 'app_dev'@'localhost' IDENTIFIED BY 'app_dev_pwd';
GRANT ALL PRIVILEGES ON app_dev_db.* TO 'app_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'app_dev'@'localhost';

FLUSH PRIVILEGES;