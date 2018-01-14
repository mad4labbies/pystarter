import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "a story of a boy",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4"
                        )
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "a marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                        )
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                        "Using rock music to learn",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=4AeUHwkIJzU"
                        )

ratatouille = media.Movie("Ratatouille",
                        "Ratatouille",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=uVeNEbh3A4U"
                        )

midnight_in_paris = media.Movie("Midnight in Paris",
                        "Midnight in Paris",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=FAfR8omt-CY"
                        )

hunger_games = media.Movie("Hunger Games",
                        "Hunger Games",
                        "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                        "https://www.youtube.com/watch?v=n-7K_OjsDCQ"
                        )

movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
#fresh_tomatoes.open_movies_page(movies)
