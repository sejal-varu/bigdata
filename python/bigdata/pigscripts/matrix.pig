m = load '/home/sejal/Documents/datascience/dataset/data/matrix/m.txt'
	using PigStorage(',')
	as (r,c,v);

n = load '/home/sejal/Documents/datascience/dataset/data/matrix/n.txt'
	using PigStorage(',')
	as (r,c,v);

j = join m by c,n by r;

p = foreach j generate m::r,n::c,m::v*n::v as v;

g = group p by (r,c);

ans_matrix = foreach g generate group.r,group.c,SUM(p.v) as sum;