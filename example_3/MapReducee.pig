hotelData = LOAD '/user/ratings.csv' using PigStorage(',') as (userId:int, movieId:int, rating:float);
hotelDataa = LOAD '/user/movies.csv' using PigStorage(',') as (movieId:int, title:chararray);
joined = join hotelDataa by movieId, hotelData by movieId;
result = GROUP joined BY title;
resultFormatted = FOREACH result GENERATE group,AVG(joined.hotelData::rating) as rate;
dump resultFormatted;
