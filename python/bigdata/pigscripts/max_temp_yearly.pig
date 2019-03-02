records = load '$input'
	using PigStorage('|')
	as (station:int,year:int,datemonth,hourminute,temprature:float);

f = filter records by temprature is not null;

p = foreach f generate year,temprature;

g = group p by year;

ans = foreach g generate group,MAX(p.temprature);

store ans into '$output';
