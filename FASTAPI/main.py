from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field 
from typing import Optional, List
import datetime

app = FastAPI()

app.title = "FastApi Prueba"
app.version = "0.0.1"

class Movie(BaseModel):
  id: int
  title: str
  overview: str
  year: int
  rating: float
  categories: list

class MovieCreate(BaseModel):
  id: int
  title: str = Field(min_length=5, max_length=15)
  overview: str = Field(min_length=15, max_length=50)
  year: int = Field(le=datetime.datetime.now().year, ge=1900)
  rating: float = Field(ge=0, le=10)
  categories: list = Field(min_items=1)

class MovieUpdate(BaseModel):
  title: str
  overview: str
  year: int
  rating: float
  categories: list


movies = [
  {
    "id": 1, 
    "title": "The Shawshank Redemption",
    "overview": "Two imprisoned",
    "year": 1994,
    "rating": 9.3,
    "categories": ["Drama","Accion","Crime"]
  },
  {
  "id": 2,
  "title": "Inception",
  "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
  "year": 2010,
  "rating": 8.8,
  "categories": ["Action", "Sci-Fi", "Thriller"]
},
{
  "id": 3,
  "title": "The Godfather",
  "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
  "year": 1972,
  "rating": 9.2,
  "categories": ["Crime", "Drama"]
},
{
  "id": 4,
  "title": "Pulp Fiction",
  "overview": "The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
  "year": 1994,
  "rating": 8.9,
  "categories": ["Crime", "Drama"]
},
{
  "id": 5,
  "title": "The Matrix",
  "overview": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
  "year": 1999,
  "rating": 8.7,
  "categories": ["Action", "Sci-Fi"]
},
{
  "id": 6,
  "title": "Parasite",
  "overview": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
  "year": 2019,
  "rating": 8.6,
  "categories": ["Comedy", "Drama", "Thriller"]
}
]



@app.get("/", tags=["Home"])
def home():
  return "Hello World!!"

@app.get("/hmtl", tags=["Home"])
def home():
  return HTMLResponse(content="<h1>Lista de Peliculas</h1>", status_code=200)

@app.get("/ListMovies", tags=["Movies"])
def list_movies()->List[Movie]:
  return movies

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int) -> Movie:
  for movie in movies:
    if movie["id"] == id:
      return movie
  return {"message": "Movie not found"}

@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str) -> Movie:
  movies_by_category = []
  for movie in movies:
    if category in movie["categories"]:
      movies_by_category.append(movie)
  return movies_by_category

@app.post("/movies", tags=["Movies"])
def create_movie(movie: MovieCreate) -> List[Movie]:
  movies.append(movie.model_dump())
  return movies

@app.put('/movies/{id}', tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> Movie:
  for item in movies:
    if item['id'] == id:
      item['title'] = movie.title
      item['overview'] = movie.overview
      item['year'] = movie.year
      item['rating'] = movie.rating
      item['categories'] = movie.categories
  return movie

@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int):
  for movie in movies:
    if movie['id'] == id:
      movies.remove(movie)
      return {"message": "Movie deleted"}
  return {"message": "Movie not found"}