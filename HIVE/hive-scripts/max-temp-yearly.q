use weather;
insert overwrite directory '/home/sejal/Documents/datascience/HIVE/weather-output'
select station_no,year,MAX(temprature)
from sensor_readings
where temprature is not null
group by station_no,year;
