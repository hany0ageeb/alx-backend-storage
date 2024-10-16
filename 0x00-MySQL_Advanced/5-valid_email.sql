-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
DROP TRIGGER IF EXISTS `after_update_users_email`;
-- CReate the trigger
CREATE TRIGGER `after_update_users_email` BEFORE UPDATE ON `users`
	FOR EACH ROW
		SET NEW.valid_email = IF(OLD.email != NEW.email, 0, NEW.valid_email);
