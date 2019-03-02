use matrix;
insert overwrite directory '/home/sejal/Documents/datascience/HIVE/matrix-output'

select temp.r,temp.c, SUM(temp.v) from
(select m.r as r, n.c as c, (m.v*n.v) as v
from m, n
where m.c = n.r
) temp
group by temp.r,temp.c;


