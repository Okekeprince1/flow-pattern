# Importing all necessary libraries
import os
# pip3 install opencv-python
import cv2

# Read the video from specified path

path = "F:\\Adelaja_UP_Thermofluid_Results\\Current videos SMOOTH TUBES 30 - 50oC_October2013_MP4"


def convertVideoToImage(path, videoPerFolder, video_name):

    cam = cv2.VideoCapture(path)

    try:

        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame
    currentframe = 0

    while(True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = './data/{}'.format(video_name) + "_" + \
                str(videoPerFolder) + "_" + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
            videoPerFolder += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
    return videoPerFolder


def readAllPaths(path):

    rootFolder = os.listdir(path)

    videoCount = 0

    while rootFolder:

        popped = rootFolder.pop()

        newPath = path + "\\" + popped
        print(newPath)

        if os.path.isdir(newPath):

            for newRoute in os.listdir(newPath):
                rootFolder.append(popped + "\\" + newRoute)
        else:
            ss = newPath.split('\\')[-1]
            if ss.startswith("Thum") == False:
                print(popped, newPath)
                naming_conv = r"{}".format(newPath).split("\\")[-1].split(" ")
                video_name = naming_conv[-2] + naming_conv[-1].replace(".mp4", "")  
                videoCount = convertVideoToImage(newPath, videoCount, video_name)

    print(videoCount)


readAllPaths(path)
