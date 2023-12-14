import cv2
import numpy as np
import time

#color detection
def seeColor(image, lower_color, upper_color):
    color_cd = []
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        n_X = x + w // 2
        n_Y = y + h // 2
            
        color_cd.append((" X: " + str(n_X), " Y: " + str(n_Y)))
        time.sleep(0.5)
        
    return color_cd


#prints blocks coordinates
def printCoord(nats,color):
    if(longer(nats) > 1):
        for i in range(len(nats[0])):
            print(color, i + 1 , " coordinates:", nats[0][i])
        print(" ")
    elif(longer(nats) == 0):
        
        pass
    else:
        print(color," coordinates:", nats[0][0],"\n")

#returns the first value of the list
def longer(arr):
    return len(arr[0])
        
#if you are using an internal camera or you dont
#have an internal camera you should change the 1 into a 0
camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while 1:
    #get the footage from the camera
    ret, footage = camera.read()
   
    #color values
    lower_blue = np.array([100, 100, 100], np.uint8)
    upper_blue = np.array([140, 255, 255], np.uint8)
    
    lower_green = np.array([50, 50, 50], np.uint8)   
    upper_green = np.array([90, 255, 255], np.uint8)
    
    
    lower_red = np.array([136, 87, 111], np.uint8) 
    upper_red = np.array([180, 255, 255], np.uint8)
    
    lower_yellow = np.array([20, 100, 100], np.uint8)
    upper_yellow = np.array([30, 255, 255], np.uint8)
    
    
    b_cd = [seeColor(footage, lower_blue, upper_blue)]
    g_cd = [seeColor(footage, lower_green, upper_green)]
    r_cd = [seeColor(footage, lower_red, upper_red)]
    y_cd = [seeColor(footage, lower_yellow, upper_yellow)]
       
    #prints the coordinates
    print("-------COORDINATES-------")
    
    printCoord(b_cd,'blue')
    printCoord(g_cd,'green')
    printCoord(r_cd,'red')
    printCoord(y_cd,'yellow')
    
    cv2.imshow('Webcam', footage)
    
    if cv2.waitKey(1)==27: 
        break

cv2.destroyAllWindows()
