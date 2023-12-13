result = 0
with open("input2.txt", "r") as file:
    for linea in file:
        line = linea.strip()
        
        line = line.split(":")
        id_game = line[0].split(" ")[1]
        line = line[1].split(";")
        num_max_red = 0
        num_max_green = 0
        num_max_blue = 0
        for game in line:
            balls = game.split(",")
            for ball in balls:
                ball = ball.split(" ")
                ball.pop(0)
                match ball[1]:
                    case "red":
                        if int(ball[0]) > num_max_red:
                            num_max_red = int(ball[0])
                    case "green":
                        if int(ball[0]) > num_max_green:
                            num_max_green = int(ball[0])
                            
                    case "blue":
                        if int(ball[0]) > num_max_blue:
                            num_max_blue = int(ball[0])
        
        result += num_max_blue*num_max_green*num_max_red
print(result)
