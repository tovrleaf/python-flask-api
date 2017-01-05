CREATE DATABASE flask_database;

CREATE USER 'flask_user'@'%' IDENTIFIED BY 'flask_password';

GRANT ALL PRIVILEGES ON flask_database.* TO 'flask_user'@'%';

DROP TABLE IF EXISTS `flask_database`.`article`;

CREATE TABLE `flask_database`.`article` (
    `id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
    `topic` VARCHAR(120) NOT NULL,
    `text` TEXT NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
