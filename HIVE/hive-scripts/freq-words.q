use comments;
insert overwrite directory '/home/sejal/Documents/datascience/HIVE/words-output'

select temp.word, COUNT(word) as repeat_freq from 
(select explode(split(line," ")) as word from books) temp
group by temp.word
order by repeat_freq desc;

