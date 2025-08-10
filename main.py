import random
import pygame

def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0 
        j = 0 
        k = 0 

        while i < len(left_arr) and j < len(right_arr):
            pygame.event.get()
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                k+=1
                i+=1
                surface.fill((0,0,0))

                draw_rects(arr,color_white)
                pygame.time.delay(30)

                pygame.display.update()
            else:
                pygame.event.get()
                arr[k] = right_arr[j]
                k+=1
                j+=1
                surface.fill((0,0,0))

                draw_rects(arr,color_white)
                pygame.time.delay(30)

                pygame.display.update()

        while i < len(left_arr):
            pygame.event.get()
            arr[k] = left_arr[i]
            k+=1
            i+=1
            surface.fill((0,0,0))

            draw_rects(arr,color_white)
            pygame.time.delay(30)

            pygame.display.update()
        
        while j < len(right_arr):
            pygame.event.get()
            arr[k] = right_arr[j]
            k+=1
            j+=1
            surface.fill((0,0,0))

            draw_rects(arr,color_white)
            pygame.time.delay(30)

            pygame.display.update()



pygame.display.set_caption('Nowfall\'s sorting viewer')

color_light = (170,170,170)
color_green = (0,255,0)
color_white = (255,255,255)
pygame.font.init()
font_moment = pygame.font.SysFont('Corbel',35)
text1 = font_moment.render('Generate' , True , (255,255,255))
text2 = font_moment.render('Insertion Sort' , True , (255,255,255))
text3 = font_moment.render('Bubble Sort' , True , (255,255,255))
text4 = font_moment.render('Selection Sort', True, (255,255,255))
text5 = font_moment.render('Merge Sort', True, (255,255,255))
# clock = pygame.time.Clock()  # A clock to limit the frame rate.
# FPS=10

surface = pygame.display.set_mode((900,600))

insertion_sorting = False
bubble_sorting = False
selection_sorting = False
merge_sorting = False
already_sorted = False
numbers = []
for i in range(90):
    numbers.append(round(random.random()*100))

def draw_rects(numbers,color):
    maxx = max(numbers)
    for i in range(len(numbers)):
        try:
            height = numbers[i]/maxx * 500
        except ZeroDivisionError:
            height = 0
        pygame.draw.rect(surface, color, (i*10, 100, 10, height))

def verify_rects(numbers,color):
    maxx = max(numbers)
    for i in range(len(numbers)):
        height = numbers[i]/maxx * 500
        pygame.draw.rect(surface, color, (i*10, 100, 10, height))
        pygame.time.delay(5)
        pygame.display.update()

running = True
while running:
    pygame.display.flip()
    mouse = pygame.mouse.get_pos()
    surface.fill((0,0,0))
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if 450 <= mouse[0] <= 900 and 0 <= mouse[1] < 50:
                insertion_sorting = True
            if 450 <= mouse[0] <= 900 and 50 <= mouse[1] <= 100:
                bubble_sorting = True
            if 225 <= mouse[0] < 450 and 0 <= mouse[1] <=50:
                selection_sorting = True
            if 225 <= mouse[0] < 450 and 50 < mouse[1] <=100:
                merge_sorting = True
            if 0 <= mouse[0] <= 225 and 0 <= mouse[1] <= 100:
                already_sorted = False
                numbers.clear()
                for i in range(90):
                    numbers.append(round(random.random()*100))

    if 450 <= mouse[0] <= 900 and 0 <= mouse[1] < 50:
        pygame.draw.rect(surface,color_light,pygame.Rect(450,0,450,50))
    elif 450 <= mouse[0] <= 900 and 50 <= mouse[1] <= 100:
        pygame.draw.rect(surface,color_light,pygame.Rect(450,50,450,50))     
    elif 0 < mouse[0] <= 225 and 0 <= mouse[1] <= 100:
        pygame.draw.rect(surface,color_light,pygame.Rect(0,0,225,100))
    elif 225 <= mouse[0] < 450 and 0 <= mouse[1] <=50:
        pygame.draw.rect(surface,color_light,pygame.Rect(225,0,225,50))
    elif 225 <= mouse[0] < 450 and 50 < mouse[1] <=100:
        pygame.draw.rect(surface,color_light,pygame.Rect(225,50,225,50))
    else:
        pygame.draw.rect(surface,(0,0,0),(450,0,450,100))
        pygame.draw.rect(surface,(0,0,0),(0,0,450,100))
    
    surface.blit(text1 , (50,50))
    surface.blit(text2, (500,15))
    surface.blit(text3, (500,65))
    surface.blit(text4, (225,15))
    surface.blit(text5, (225,65))
    if insertion_sorting == False and bubble_sorting == False and selection_sorting == False and merge_sorting == False:
        draw_rects(numbers,color_white)
    elif insertion_sorting == True:
        if already_sorted == False:
            for i in range(1,len(numbers)):
                pygame.event.get()
                temp = numbers[i]
                left = i-1
                while left >= 0: #i had it as left > 0  and it wouldnt work so because it wouldnt flip the first thing so yeah >=0
                    if numbers[left] > temp:
                        numbers[left+1],numbers[left]=numbers[left],temp
                        surface.fill((0,0,0))
                        draw_rects(numbers,color_white)
                        pygame.time.delay(5)

                        pygame.display.update()
                    left-=1
        draw_rects(numbers,color_white)
        verify_rects(numbers,color_green)
        insertion_sorting = False
        already_sorted = True

    elif bubble_sorting == True:
        if already_sorted == False:
            n = len(numbers)
            for i in range(n):
                pygame.event.get()
                for j in range(n-i-1):
                    if numbers[j]> numbers[j+1]:
                        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

                        surface.fill((0,0,0))
                        draw_rects(numbers,color_white)
                        pygame.time.delay(5)

                        pygame.display.update()
        draw_rects(numbers,color_white)
        verify_rects(numbers,color_green)
        bubble_sorting = False
        already_sorted = True

    elif selection_sorting == True:
        if already_sorted == False:
            for i in range(len(numbers)):
                pygame.event.get()
                smin = i
                for j in range(i+1,len(numbers)):
                    if numbers[j] < numbers[smin]:
                        smin = j
                numbers[i],numbers[smin]=numbers[smin],numbers[i]
                surface.fill((0,0,0))
                draw_rects(numbers,color_white)
                pygame.time.delay(30)

                pygame.display.update()

        draw_rects(numbers,color_white)
        verify_rects(numbers,color_green)
        selection_sorting = False
        already_sorted = True

    elif merge_sorting == True:
        merge_sort(numbers)
        draw_rects(numbers,color_white)
        verify_rects(numbers,color_green)
        merge_sorting = False
        already_sorted = True

    
