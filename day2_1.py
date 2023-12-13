result = 0
with open("input2.txt", "r") as file:
    for linea in file:
        line = linea.strip()
        
        line = line.split(":")
        id_game = line[0].split(" ")[1]
        line = line[1].split(";")
        no_game_no_gain = True
        for game in line:
            balls = game.split(",")
            for ball in balls:
                ball = ball.split(" ")
                ball.pop(0)
                match ball[1]:
                    case "red":
                        if int(ball[0]) > 12:
                            no_game_no_gain = False
                            break
                    case "green":
                        if int(ball[0]) > 13:
                            no_game_no_gain = False
                            break
                    case "blue":
                        if int(ball[0]) > 14:
                            no_game_no_gain = False
                            break
        if no_game_no_gain:
            result += int(id_game)
print(result)
