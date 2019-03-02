use facebook_logs;
insert overwrite directory '/home/sejal/Documents/datascience/HIVE/fb-output'
select email, action, count(email)
from facebook_logs
group by email, action;

