-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Requirements:
-- 	1. Import this table dump: metal_bands.sql.zip (https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ)
--	2. Column names must be: origin and nb_fans
--	3. our script can be executed on any database
SELECT `origin`, SUM(`fans`) as nb_fans
FROM  `metal_bands`
GROUP BY `origin`
ORDER BY nb_fans DESC;
