-- creating user, setting pass,  granting user

CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED AS 'user_0d_1_pwd'
GRANT ALL PRIVILAGES ON *.* TO 'user_0d_1'@'localhost';
