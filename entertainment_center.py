import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys taht come to life", 'http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg', 'https://www.youtube.com/watch?v=KYz2wyBy3kc')

inception = media.Movie("Inception", "A story of people hacking into dream", "http://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Inception_ver3.jpg/220px-Inception_ver3.jpg", "https://www.youtube.com/watch?v=66TuSJo4dZM")

her = media.Movie("Her", "A story of the near future and a man who falls in love with AI", "http://upload.wikimedia.org/wikipedia/en/thumb/4/44/Her2013Poster.jpg/220px-Her2013Poster.jpg", "https://www.youtube.com/watch?v=WzV6mXIOVl4")

movies = [toy_story, inception, her]
fresh_tomatoes.open_movies_page(movies)
