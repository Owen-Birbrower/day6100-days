print("\033[38;5;208m", "==New York Knick Player Box Score Predictor==", "\033[0m")
print("\033[38;5;27m", "This is a powerfool tool. Before we begin lets varify you know ball.", "\033[0m")
password = input("Is brunson top 10 all time? ")
rings = input("How many rings will the knicks win in the next three yrs (0, 1, 2, 3)? ")
if (password == "yes" or password == "duh") and not (rings == "0"):
  print("You know ball")
else:
  print("You don't know ball")

player = input("INQUIRE - Enter a NYK player: ")
if player == "brunson":
  print("40p 8a")
elif player == "hart":
  print("16p 16r 10a")
elif player == "og":
  print("22p 4r 4a 4s/b")
elif player == "kat":
  print("34p 15r")
elif player == "bridges":
  print("25p")
else:
  print("Thibs gave ", player, " 0 min")
