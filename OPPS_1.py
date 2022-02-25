class Movie_Blast:
    Type = "Movie_Blast"
    def print(self):
        print(f"Name is {self.name}")
        print(f"Type is {self.type}")
        print(f"Type is {self.IMD_rating}")
        
PrasadReview = Movie_Blast()
PrasadReview.name = "Shawshank Resemption"
PrasadReview.type = "The Greatest Movie ever made"
PrasadReview.IMD_rating = "It has The Highest of 9.3 Stars"
PrasadReview.print()