# sportsmanagment

download :pip install pillow
pip install mysql-connector-python



database:

mysql>
mysql> USE sports_management;
Database changed
mysql>
mysql> CREATE TABLE Players (
    ->     player_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     username VARCHAR(50) NOT NULL,
    ->     phone VARCHAR(15),
    ->     place VARCHAR(100),
    ->     password VARCHAR(50) NOT NULL
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> CREATE TABLE Coaches (
    ->     coach_id VARCHAR(10) PRIMARY KEY,
    ->     username VARCHAR(50) NOT NULL,
    ->     phone VARCHAR(15),
    ->     place VARCHAR(100),
    ->     password VARCHAR(50) NOT NULL
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> CREATE TABLE Equipment (
    ->     equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     equipment_name VARCHAR(100) NOT NULL,
    ->     sport_name VARCHAR(50) NOT NULL
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> CREATE TABLE Events (
    ->     event_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     event_name VARCHAR(100) NOT NULL,
    ->     sport_name VARCHAR(50) NOT NULL,
    ->     event_date DATE NOT NULL
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> CREATE TABLE Teams (
    ->     team_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     team_name VARCHAR(100) NOT NULL,
    ->     sport VARCHAR(50) NOT NULL,
    ->     captain_id INT,
    ->     FOREIGN KEY (captain_id) REFERENCES Players(player_id)
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> CREATE TABLE TeamMembers (
    ->     team_id INT,
    ->     player_id INT,
    ->     role VARCHAR(20),
    ->     PRIMARY KEY (team_id, player_id),
    ->     FOREIGN KEY (team_id) REFERENCES Teams(team_id),
    ->     FOREIGN KEY (player_id) REFERENCES Players(player_id)
    -> );
Query OK, 0 rows affected (0.02 sec)
