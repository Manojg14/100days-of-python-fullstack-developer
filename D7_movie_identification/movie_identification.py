movie_actor ={
     "thalapathi" : "Rajinikanth", "naadodigal" : "Sasikumar", "jailer" : "Rajinikanth", "leo" : "Vijay","vikram" : "Kamal Hasan",
     "amaran"     : "Sivakarthikeyan", "viswasam" : "Ajith Kumar", "thangalaan" : "Vikram", "miss You" : "Siddharth", "jayam" : "Jayam Ravi"
             }

yearrealesed_movie ={
     "thalapathi" : 1991, "naadodigal" : 2009, "jailer" : 2023, "leo" : 2023, "vikram" : 2022, "amaran"  : 2024,"viswasam" : 2019,
     "thangalaan" : 2024, "miss You"   : 2025, "jayam"  : 2003
                   }



def movie_details(movie_name):
    # check movie name is present at two variable or not

    if movie_name in movie_actor and movie_name in yearrealesed_movie:
        actor = movie_actor[movie_name]
        year = yearrealesed_movie[movie_name]
        return f"Movie Name : {movie_name}, Actor Name : {actor}, Year : {year}"
    else:
        return "enter invalid input"

# movie name display
movie_list = list(movie_actor.keys())
print(f"Movie List:",movie_list)

# get the input of the movie name
movie_name = input("enter the movie name:").lower()
print(movie_details(movie_name))
print(movie_actor.values())


