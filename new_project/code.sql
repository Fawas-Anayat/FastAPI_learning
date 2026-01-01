CREATE DATABASE fastapi_database;
CREATE USER 'fastapi_user'@'localhost' IDENTIFIED BY 'Pakistan123';
GRANT ALL PRIVILAGES ON fastapi_database.* TO 'fastapi_user'@'localhost';
FLUSH PRIVILAGES
