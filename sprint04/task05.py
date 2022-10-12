# The basic premise of the game Gallows is to follow two rules:
# First character of next word must match last character of previous word.
# The word must not have already been said.

class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if not self.words or word not in self.words and word[0] == self.words[-1][-1]:
            self.words.append(word)
        
            return self.words
        
        else:
            self.game_over = True
        
            return 'game over'

    def restart(self):
        self.words.clear()
        self.game_over = False
        
        return 'game restarted'
