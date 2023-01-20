from mrjob.job import MRJob

class MRHotelMapReduce(MRJob):
    
    def mapper(self, _, line):
        (userId, movieId, rating, timestamp) = line.split(",")
        if(userId!="userId"):
            result = [movieId, float(rating)]
            yield result
        

    def reducer(self, key, values):
        suma=0
        suma2=0
        for value in values:
            suma2+=value
            suma+=1
        result = [key, suma2/suma]
        yield result

if __name__ == '__main__':
    MRHotelMapReduce.run()