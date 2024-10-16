--  SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
-- Requirements:
-- 	1. Procedure AddBonus is taking 3 inputs (in this order):
--		1.1 user_id, a users.id value (you can assume user_id is linked to an existing users)
--		1.2 project_name, a new or already exists projects - if no projects.name found in the table, you should create it
--		1.3 score, the score value for the correction
DROP PROCEDURE IF EXISTS `AddBonus`;
DELIMITER $$
CREATE PROCEDURE `AddBonus` (IN user_id INT, IN project_name varchar(255), IN score INT)
BEGIN
	DECLARE project_id INT DEFAULT NULL;
	SELECT `id` INTO project_id FROM `projects` WHERE `name` = project_name;
	IF project_id IS NULL
	THEN
		INSERT INTO `projects`(`name`) VALUES (project_name);
		SELECT `id` INTO project_id FROM `projects` WHERE `name` = project_name;
	END IF;
	INSERT INTO `corrections`(`user_id`, `project_id`, `score`) VALUES (user_id, project_id, score);
END $$
DELIMITER ;
