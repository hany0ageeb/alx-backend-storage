-- SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
-- Requirements:
-- 	1. You must create a function
--	2. The function SafeDiv takes 2 arguments:
--		2.1 a, INT
--		2.2 b, INT
--	3. And returns a / b or 0 if b == 0
DROP FUNCTION IF EXISTS SafeDiv;
delimiter $$
CREATE FUNCTION SafeDiv(a INT,b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	RETURN IF(b = 0, 0, a /b);
END;
$$
delimiter ;
