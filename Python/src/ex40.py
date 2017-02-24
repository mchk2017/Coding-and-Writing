#   Exercise 40: Modules, Classes, and Objects

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print 20 * '-'
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

song_lyrics = Song(["It's been a long day without you my friend",
"And I'll tell you all about it when I see you again",
"We've come a long way from where we began",
"Oh I'll tell you all about it when I see you again",
"When I see you again"])

song_lyrics.sing_me_a_song()
