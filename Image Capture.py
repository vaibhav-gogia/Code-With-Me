from time import time
import cv2 as cv
import os
  
# Opens the inbuilt camera of laptop to capture video.
cap = cv.VideoCapture(0)
i = 0

#Specify path where image needs to be saved  
path = r"C:\Users\vaigogia\OneDrive - Advanced Micro Devices Inc\Documents\GitHub\Python Automation\New folder\ChipScrubber\Images"
while(cap.isOpened()):
    for j in range(50): #Specify this number for the number of images needed
        ret, frame = cap.read()
      
    # This condition prevents from infinite looping 
    # incase video ends.
        if ret == False:
            break
      
    # Save Frame by Frame into disk using imwrite method
        #cv.imwrite(str(path) + "Frame"+str(i)+'.jpg', frame)
        cv.imwrite(os.path.join(path, 'Frame'+str(i)+'.jpg'), frame)
        i += 1
    break

  
cap.release()
cv.destroyAllWindows()


#Alternate methods used below. IGNORE THEM FOR NOW.

# # Create a new VideoCapture object
# cam = cv.VideoCapture(0)

# # Initialise variables to store current time difference as well as previous time call value
# previous = time()
# delta = 0

# # Keep looping
# while True:
#     # Get the current time, increase delta and update the previous variable
#     current = time()
#     delta += current - previous
#     previous = current

#     # Check if 3 (or some other value) seconds passed
#     if delta > 2:
#         # Operations on image
#         # Reset the time counter
#         cv.imwrite("Frame.png", img)
#         delta = 0

#     # Show the image and keep streaming
#     _, img = cam.read()
#     cv.imshow("Frame", img)
#     cv.imwrite("Frame.png", img)
#     cv.waitKey(1)
    
    
#IGNORE FOR NOW:
    
# import cv2 as cv
  
# # initialize the camera

# cam_port = 0
# cam = cv.VideoCapture(cam_port)
  
# # reading the input using the camera
# result, image = cam.read()
  
# # If image will detected without any error, 
# # show result
# if result:
  
#     # showing result, it take frame name and image 
#     # output
#     cv.imshow("Pic1", image)
  
#     # saving image in local storage
#     cv.imwrite("Pic1.png", image)
  
#     # If keyboard interrupt occurs, destroy image 
#     # window
#     cv.waitKey(0)
#    # cv.destroyWindow("Pics1")
  
# # If captured image is corrupted, moving to else part
# else:
#     print("No image detected. Please! try again")
