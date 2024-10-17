-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- Requirements:
-- 	1. Procedure ComputeAverageScoreForUser is taking 1 input:
--		1.1 user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS `ComputeAverageScoreForUser`;
delimiter $$
CREATE PROCEDURE `ComputeAverageScoreForUser`(IN user_id INT)
BEGIN
	UPDATE `users`
	SET `average_score` = (
		SELECT IFNULL(AVG(`corrections`.`score`), 0)
		FROM `corrections`
		WHERE `corrections`.`user_id` = user_id
		GROUP BY `corrections`.`user_id`)
	WHERE `users`.`id` = user_id;
END
$$
delimiter ;
