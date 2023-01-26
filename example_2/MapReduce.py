from mrjob.job import MRJob

class MRHotelMapReduce(MRJob):
    
    def mapper(self, _, line):
        (userId, movieId, rating, timestamp) = line.split(",")
        if(userId!="userId"):
            result = [movieId, float(rating)]
            yield result
        

    def reducer(self, key, value):
        ratinglist = list(value)
        yield key, sum(ratinglist)/len(ratinglist)
if __name__ == '__main__':
    MRHotelMapReduce.run()