-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
-- Requirements:
--	1. Procedure ComputeAverageWeightedScoreForUsers is not taking any input
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
delimiter $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE `users`
	SET `users`.`average_score` = (
		SELECT SUM(`corrections`.`score` * `projects`.`weight`) / SUM(`projects`.`weight`)
		FROM `projects` INNER JOIN `corrections`
			ON `projects`.`id` = `corrections`.`project_id`
		WHERE `corrections`.`user_id` = `users`.`id`
	);
END;
$$
delimiter ;
