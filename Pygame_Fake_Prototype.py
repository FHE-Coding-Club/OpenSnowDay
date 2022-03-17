# Python Prototype of the Snow Day Guesser by Olin

#I know its not really what we are looking for but I thought it would be fun to recreate the current system of "Snow Day Calculator" 
#(other) than what I think they really do is take a guess and random number generate for each USA state idk
#To get to the point I can do whatever in this project weather (pun not intended) it be sever side or try to do something else
#
#I am happy to be a part of the team
#
#oh and if you want a pure console printed version instead of a Pygame application just ask (idk why you would want it but I don't care)

# Libs
from cgitb import reset
from math import fabs
import pygame
import python_weather
import asyncio
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
base_font = pygame.font.Font(None, 32)
user_text = ''
other1_text = 'City Name :'
reault = ''

input_rect = pygame.Rect(200,200,140,32)

async def getweather(namelol):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)
    snowday = False

    # fetch a weather forecast from a city
    weather = await client.find(namelol)

    # current day's forecast temperature (int) == my strang testing stuff 
    #
    #It should be pretty close but not exact
    print(weather.current.temperature)

    if (weather.current.temperature <= -15):
        print("You could have a Snow Day (I think)")
        snowday = True

    # Sees if the weather will make it a snow day
    if snowday == False:
        for forecast in weather.forecasts:
            
            if forecast.sky_text == "Snow Showers":
                snowday = True
                print(str(forecast.date), "I think you could have a Snow Day")

            elif forecast.sky_text == "Light Snow":
                snowday = True
                print(str(forecast.date), "I don't think you will but maybe you could have a Snow Day")

            elif forecast.sky_text == "Heavy Snow":
                snowday = True
                print(str(forecast.date), "I think you could have a Snow Day")

            else:
                print(str(forecast.date), "no Snow Day sorry")

    await client.close()


# Game Loop lol
running = True
while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #Deleting Stuff
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            #Press Enter to run the Weather Method
            elif event.key == pygame.K_RETURN:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(getweather(user_text))

                user_text = ''
            else:
                #Type the city you want
                user_text += event.unicode
            
            #Quit stuff
            if event.key == pygame.K_ESCAPE:
                running = False
    

    # Display
    screen.fill((0, 0, 0))
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    other1_surface = base_font.render(other1_text, True, (255, 255, 255))
    reault_surface = base_font.render(reault, True, (255, 255, 255))


    screen.blit(text_surface,(10,25))
    screen.blit(reault_surface,(10,50))
    screen.blit(other1_surface,(0,0))

    # Flip the display wooooo
    pygame.display.flip()

# Done! Ez
pygame.quit()
