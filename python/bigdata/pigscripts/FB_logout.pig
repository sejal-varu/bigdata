records = load '$input'
	using PigStorage(',')
	as (email,datetime:int,hourminute:int,inout);

f = filter records by inout == 'out';

p = foreach f generate email,inout;

g = group p by email;

ans = foreach g generate group as username,COUNT(p) as no_of_outs;

store ans into '$output';