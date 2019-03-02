rec1 = load '/home/sejal/Documents/datascience/dataset/data/weather_data/weather_data_set_1900'
	using PigStorage('|')
	as (station:int,year:int,datemonth,hourminute,temprature:float);

rec2 = load '/home/sejal/Documents/datascience/dataset/data/weather_data_company_xyz/weather_data_set'
	using PigStorage(',')
	as (year:int,temprature:float);


f = filter rec1 by temprature is not null;

p = foreach f generate year,temprature;

f2 = filter rec2 by temprature is not null;

u = UNION onschema p,f2;

g = group u by year;

ans = foreach g generate group,MAX(u.temprature);