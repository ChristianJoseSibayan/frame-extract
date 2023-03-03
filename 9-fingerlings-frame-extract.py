# 1. Import Libraries
import cv2
import os

# 2. Read the video from the specified path
vid = cv2.VideoCapture(
    'C:/Users/Christian/Desktop/extract-frame/9-confirmed-fingerlings.mp4')
# 3. Create folder to save the extracted frames
try:
    if not os.path.exists('frames'):
        os.makedirs('frames')
except OSError:
    print('Error: Creating directory of the frames')

# 4. Create variables to monitor the frame and to set the interval
current_frame = 0
frame_interval = 60

# 5. Read the frames from the video
while True:
    success, frame = vid.read()

    if success:
        # 6. Check the current frame if it is a mulitiple of the frame interval
        if current_frame % frame_interval == 0:
            # 7. Continue extracting frame until the video ends
            name = './frames/frame' + str(current_frame) + '.jpg'
            print('Creating...' + name)

            # 8. Save/Write the extracted images
            cv2.imwrite(name, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])

        # 9. Increase the current frame to show how many frames are created
        current_frame = current_frame + 1
    else:
        break

# 10. Release all space and windows once done
vid.release()
cv2.destroyAllWindows()
