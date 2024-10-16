-- SQL script that creates a table users following these requirements:
-- 1. With these attributes:
--	1.1 id, integer, never null, auto increment and primary key
--	1.2 email, string (255 characters), never null and unique
--	1.3 name, string (255 characters)
-- 	1.4 country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
-- 2. If the table already exists, your script should not fail
-- 3. Your script can be executed on any database
CREATE TABLE IF NOT EXISTS `users` (
	`id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`email` VARCHAR(255) NOT NULL UNIQUE,
	`name` VARCHAR(255) NULL,
	`country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
