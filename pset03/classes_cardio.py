

import math



class Rectangle:
    def __init__(self, length, width):
     self.width = width
     self.length = length

    def area(self):
     if self.width and self.length > 0:
         return self.width * self.length
    
    def perimeter(self):
     if self.width and self.length > 0:
        return(self.width * 2) + (self.length * 2)
        
    def __str__(self):
         return f"Rectangle({self.length} x {self.width})"

    


class Circle:
 def __init__ (self, radius):
   self.radius = radius

 def area(self):
   if self.radius > 0:
    return math.pi * (self.radius**2)

 def circumference(self):
   if self.radius > 0:
      return 2 * math.pi * self.radius 

 def __str__(self):
   return f"Circle(radius={self.radius})"





class Song:
   def __init__(self, title, artist, duration):
      self.title= title
      self.artist= artist
      self.duration= duration

   def play(self):
      print (f"Playing {self.title} by {self.artist} ({self.duration}s)")

   def __str__(self):
      return f"{self.title} by {self.artist} ({self.duration}s)"
      





class Playlist:

    
  
 def __init__(self):
       self.playlist = []

 def add_song(self,song):
      self.playlist.append(song)


 def __str__(self):
    song_strings= []
    if len(self.playlist) <= 0:
      return f"Playlist is empty"
    else:
     for s in self.playlist:
       song_strings.append(str(s))
       result= "|".join(song_strings)
       
    return result
    

 def play_all(self):
     for s in self.playlist:
      s.play()

 
 
    
      

    

      
      




def test_rectangle():
    rect = Rectangle(3, 4)
    assert rect.area() == 12
    assert rect.perimeter() == 14
    assert str(rect) == "Rectangle(3 x 4)"


def test_circle():
    circle = Circle(5)
    assert circle.area() == 25*math.pi
    assert circle.circumference() == 10*math.pi
    assert str(circle) == "Circle(radius=5)"


def test_song(capfd):
    song = Song("Night Shift", "Lucy Dacus", 391)
    assert str(song) == "Night Shift by Lucy Dacus (391s)"
    song.play()
    captured_output = capfd.readouterr()
    assert captured_output.out == (
        "Playing Night Shift by Lucy Dacus (391s)\n"
    )


def test_playlist(capfd):
    playlist = Playlist()
    song1 = Song("Night Shift", "Lucy Dacus", 391)
    song2 = Song("I Was Neon", "Julia Jacklin", 243)
    song3 = Song("Forgiveness", "Alice Glass", 191)
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    assert str(playlist) == (
        "Night Shift by Lucy Dacus (391s)|"
        "I Was Neon by Julia Jacklin (243s)|"
        "Forgiveness by Alice Glass (191s)"
    )
    playlist.play_all()
    captured_output = capfd.readouterr()
    assert captured_output.out == (
        "Playing Night Shift by Lucy Dacus (391s)\n"
        "Playing I Was Neon by Julia Jacklin (243s)\n"
        "Playing Forgiveness by Alice Glass (191s)\n"
    )
