# import all our required modules
import media
import fresh_tomatoes
import SimpleHTTPServer
import SocketServer

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


# define favorite movies from the Movie class
DARK_KNIGHT = media.Movie(
    "The Dark Knight",
    "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

INTERSTELLAR = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=2LqzF5WauAw")

GLADIATOR = media.Movie(
    "Gladiator",
    "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcRuhegCaGHfcQc-Owpib9vGSO0hUlSUMTojO2s4ih8oXqHBw2ks",
    "https://www.youtube.com/watch?v=ol67qo3WhJk")

WALLE = media.Movie(
    "WALL*E",
    "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=alIq_wG9FNk")

PULP_FICTION = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

REQUIEM_DREAM = media.Movie(
    "Requiem For A Dream",
    "The drug-induced utopias of four Coney Island people are shattered when their addictions run deep.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BOTdiNzJlOWUtNWMwNS00NmFlLWI0YTEtZmI3YjIzZWUyY2Y3XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=0nU7dC9bIDg")

THE_MATRIX = media.Movie(
    "The Matrix",
    "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

movies = [DARK_KNIGHT,INTERSTELLAR,WALLE,GLADIATOR,PULP_FICTION,REQUIEM_DREAM,THE_MATRIX]


httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT

fresh_tomatoes.construct_movie_page(movies, str(PORT))

httpd.serve_forever()