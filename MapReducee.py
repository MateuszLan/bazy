from mrjob.job import MRJob

class MRHotelMapReducee(MRJob):
    
    def mapper(self, _, line):
        (userId, movieId, rating, timestamp) = line.split(",")
        if(userId!="userId"):
            with open("C:\\Users\\vdi-terminal\\Downloads\\bazy-main\\example_2\\movies.csv", "r", encoding="utf-8") as movie_titles:
                for title in movie_titles:
                    title_parts = title.strip().split(",")
                    if title_parts[0]!="movieId":
                        if title_parts[0] == movieId:
                            movie_title = title_parts[1]
                            break
            result = [movie_title, float(rating)]
            yield result
        

    def reducer(self, key, value):
        ratinglist = list(value)
        yield key, sum(ratinglist)/len(ratinglist)
if __name__ == '__main__':
    MRHotelMapReducee.run()
