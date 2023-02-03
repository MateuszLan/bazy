hotelData = LOAD '/user/ratings.csv' using PigStorage(',') as (userId:int, movieId:int, rating:float);
result = GROUP hotelData BY movieId;
resultFormatted = FOREACH result GENERATE group as movieId,AVG(hotelData.rating) as rate;
dump resultFormatted;
