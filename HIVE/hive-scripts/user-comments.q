use comments;
insert overwrite directory '/home/sejal/Documents/datascience/HIVE/comments-output'
select u.gender as g,COUNT(u.gender)
from users u, comments c
where u.id = c.userid
group by u.gender;

/* Get distint username
select DISTINCT u.username
from users u, comments c
where u.id = c.userid;
*/
