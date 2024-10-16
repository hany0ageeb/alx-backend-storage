-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
-- Drop trigger if exists
DROP TRIGGER IF EXISTS `ins_order`;
-- create trigger per specifications
CREATE TRIGGER `ins_order` AFTER INSERT ON `orders`
	FOR EACH ROW
		UPDATE `items`
		SET `items`.`quantity` = `items`.`quantity` - NEW.number
		WHERE `items`.`name` = NEW.item_name;
