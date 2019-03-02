lines = load '/home/sejal/Documents/datascience/dataset/data/words/text_data.txt'
	as (line:chararray)

words =  foreach lines generate flatten(TOKENIZE(line)) AS word;

f = filter words by (word !='the') and (word !='and');

g = group words by word;

count = foreach g generate group as word,COUNT(f) as wordcount;

o = order count by wordcount desc;

ans = limit o to 20;
