users = load '/home/sejal/Documents/datascience/dataset/data/userComments/users.txt'
	using PigStorage(',')
	as (userid:long,username:chararray,address,gender:chararray);

comments = load '/home/sejal/Documents/datascience/dataset/data/userComments/comments.txt'
	using PigStorage(',')
	as (userid:long,comments_desc:chararray,date,likes);

j = join users by userid,comments by userid;

p = foreach j generate users::gender as gender,users::userid as userid;

g = group p by email;

ans = foreach g generate group as gender,COUNT(p) as total_comments_made;