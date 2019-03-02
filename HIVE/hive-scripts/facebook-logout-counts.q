use facebook_logs;
insert overwrite directory '/home/sejal/Documents/datascience/HIVE/fb-output'
select email,COUNT(email) as logouts
from facebook_logs
where action='out'
group by email
order by logouts desc;
