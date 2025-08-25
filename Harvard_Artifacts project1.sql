create database Harvard_Artifactse;

use Harvard_Artifactse;


SELECT * FROM artifact_metadata;
SELECT * FROM artifact_media;
select*from  artifact_colors;

-- 1. Artifacts from 17th century & Japanese culture
SELECT * FROM artifact_metadata
WHERE century = '17th century'
AND culture = 'Japanese';


-- 2 Unique cultures represented
SELECT DISTINCT culture 
FROM artifact_metadata
WHERE culture IS NOT NULL;

-- 3  Artifacts from the Archaic Period
SELECT * FROM artifact_metadata
WHERE period = 'Edo period, 1615-1868';

-- 4  Artifact titles ordered by accession year (descending)
SELECT title FROM artifact_metadata
ORDER BY accessionyear DESC;

-- 5 Artifact count per department
SELECT department, COUNT(*) AS artifact_count
FROM artifact_metadata
GROUP BY department;
------------------------
-- artifact_media Table 
-- 6 Which artifacts have more than 3 images
select*from artifact_media;

SELECT * FROM artifact_media 
WHERE imagecount > 3;

-- 7 What is the average rank of all artifacts --
select avg('rank') from artifact_media;

-- 8 Which artifacts have a less mediacount than colorcount --
SELECT * FROM artifact_media
WHERE mediacount < colorcount;

-- 9 List all artifacts created between 1500 and 1600
select*from artifact_media
where datebegin >= 1500 and  dateend <= 1600;

-- 10 How many artifacts have no media files
select count(*) AS no_media_count 
from artifact_media
where  mediacount = 0;

-- 11 What are all the distinct hues used in the dataset
select*from artifact_colors;
SELECT DISTINCT color
FROM artifact_colors;

-- 12 What are the top 5 most used colors by frequency
SELECT color, COUNT(*) AS frequency
FROM artifact_colors
GROUP BY color
ORDER BY frequency DESC
LIMIT 5;

-- 13 What is the average coverage percentage for each hue
SELECT color, AVG('colorpercentage') AS avg_percentage
FROM artifact_colors
GROUP BY color
ORDER BY avg_percentage DESC;

-- 14 List all colors used for a given artifact ID
select*FROM artifact_colors
WHERE objectid = 192476;


-- 15 What is the total number of color entries in the dataset
SELECT COUNT(*) AS total_color_entries
FROM artifact_colors;

-- 16 List artifact titles and hues for all artifacts belonging to the Byzantine culture.
SELECT m.title, c.hue
FROM artifact_metadata m
JOIN artifact_colors c ON m.id = c.objectid
WHERE m.culture = 'Byzantine';

-- 17 List each artifact title with its associated hues.
SELECT m.title, c.hue
FROM artifact_metadata m
JOIN artifact_colors c ON m.id = c.objectid;

-- 18 Get artifact titles, cultures, and media ranks where the period is not null.
SELECT m.title, m.culture, me.rank
FROM artifact_metadata m
JOIN artifact_media me ON m.id = me.objectid
WHERE m.period IS NOT NULL;

-- 19 Find artifact titles ranked in the top 10 that include the color hue "Grey".
SELECT T1.title, T2.hue, T3.rank
FROM artifact_metadata AS T1
JOIN artifact_colors AS T2 ON T1.id = T2.objectid
JOIN artifact_media AS T3 ON T1.id = T3.objectid
WHERE T2.hue = 'Grey'
ORDER BY T3.rank DESC
LIMIT 10;




-- 20 How many artifacts exist per classification, and what is the average media count for each?
SELECT m.classification,COUNT(*) AS total_artifacts,
AVG(me.mediacount) AS avg_media_count
FROM artifact_metadata m
JOIN artifact_media me ON m.id = me.objectid
GROUP BY m.classification;

-- 21. Find all artifacts that have a known medium
SELECT * FROM artifact_metadata
WHERE medium IS NOT NULL;

-- 22 Count the number of unique periods recorded
SELECT COUNT(DISTINCT period) AS unique_periods
FROM artifact_metadata;


-- 23 List all artifact titles that belong to the "Paintings" classification
SELECT title, classification FROM artifact_metadata 
WHERE classification = 'Paintings';


-- 24 Show the earliest and latest accession years
SELECT MIN(accessionyear) AS earliest_accession,
MAX(accessionyear) AS latest_accession FROM artifact_metadata;

-- 25. Find all artifacts where the department contains the word Harvard University Portrait Collection
SELECT * 
FROM artifact_metadata
WHERE department = 'Harvard University Portrait Collection';




