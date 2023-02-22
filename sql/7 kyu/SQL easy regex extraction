ALTER TABLE greetings
ADD COLUMN user_id varchar;

UPDATE greetings
SET user_id = CAST(substring(greeting from '#(\d+)') AS varchar)
WHERE greeting ~ '#\d+';

select name,greeting,user_id from greetings;