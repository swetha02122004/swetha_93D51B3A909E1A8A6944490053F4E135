class player:
  def play(self):
    print("the player is playing cricket")

class batsman(player):
  def play(self):
    print("the batsman is batting")

class bowler(player):
  def play(self):
    print("the bowler is bowling")

B=batsman()
b=bowler()
p=player()

B.play()
b.play()
p.play()