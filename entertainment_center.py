import media
import fresh_tomatoes

# each of the movies instantiated as hardcode

matrix = media.Movie("The Matrix",
                       "A man discovers computers control his existence",
                       "http://thebitplayers.net/wp-content/uploads/2015/08/the-matrix-movie-poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=m8e-FF8MsqU")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg",   # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

kingsspeech = media.Movie("The King's Speech",
                           "A man befriends the king in 1940s England",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMzU5MjEwMTg2Nl5BMl5BanBnXkFtZTcwNzM3MTYxNA@@._V1_UY268_CR0,0,182,268_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=pzI4D6dyp_o")

frozen = media.Movie("Frozen",
                  "Disney comes up with some good songs in a mediocre movie",
                  "http://www.tammileetips.com/wp-content/uploads/2013/09/Disney-Frozen-Movie-Poster.png",   # NOQA
                  "https://www.youtube.com/watch?v=TbQm5doF_Uc")

paris = media.Movie("Midnight in Paris",
                    "Owen Wilson joins Woody Allen in a sweet story about"
                    " a dude that goes back in time in Paris"
                    " and meets Hemingway",
                    "http://www.impawards.com/2011/posters/midnight_in_paris_xlg.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=BYRWfS2s2v4")

startrek = media.Movie("Star Trek Into Darkness",
                     "Sherlock Holmes becomes an intergalactic terrorist",
                     "http://3.bp.blogspot.com/-UB3u4fAXFJY/UemEN-dZSiI/AAAAAAAATLw/ZzTeo3EPln0/s1600/Star+Trek+Into+Darkness+DVD.jpg",   # NOQA
                     "https://www.youtube.com/watch?v=r5gdbUC9mWU")

# list of classes to pass for display
movies = [matrix, avatar, kingsspeech, frozen, paris, startrek]

# create and launch website using rottentomatoes.py dependency
fresh_tomatoes.open_movies_page(movies)
