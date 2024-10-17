-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
-- Requirements:
--	1. Procedure ComputeAverageScoreForUser is taking 1 input:
--		1.1 user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
delimiter $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	UPDATE `users`
	SET `users`.`average_score` = (
		SELECT SUM(score * weight) / SUM(weight)
		FROM `projects` INNER JOIN `corrections`
			ON `projects`.`id` = `corrections`.`project_id`
		WHERE `corrections`.`user_id` = user_id)
	WHERE `users`.`id` = user_id;
END;
$$
delimiter ;
