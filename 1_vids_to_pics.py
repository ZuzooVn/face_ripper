'''
Using OpenCV takes a mp4 video and produces a number of images.
---------- [ONLY USES FACES OF PEOPLE OVER 18]
A WORD ABOUT SELECTING VIDEOS FOR FACE SCRAPING:
Ideal videos for your target face videos are not 2GB, 120 minute files of the face owner staring in entire movies,
Rather, a range of different shorter clips with the target face giving a lot of 1080p face time in a range of emotions.

For example: You'll get better speed and quality ripping climactic, three minute scenes of Kristen Stewart from Twilight,
and 1080p Kristen Stewart five minute interviews rather than to feed entire movies like Twighlight through this process.
----------

After you have assembled your dozen(s) (of) mp4 video clips into one file, make a backup of them and run this script.
Your file of videos will be selected by this script on line 40. Replace the path on line 40 with your video file's path.
Replace each video file with a folder of photos of every from of your video. This go in the same folder as your video's.
This path is on 34, 35, and 51. A new folder called 'vidpics' with a number at the end (ex 'vidpics1') will be created
for each video.

This is going to remove each mp4 file after using it, so that it doesn't render the same video twice.
So make a backup of videos before use.
The output images this script creates are the input images in the next script, 2_copy.py
'''
import cv2
import glob
import uuid
import os, random
import numpy as np

count = 1
count2 = 1
# Range number is the number of videos in your file you'll be replacing with a folder full of it's frames as jpgs:
for i in range(9):
	try:
		try:
			if not os.path.exists('/PATH/CREATING/JPG/OUTOUT/DIR/vidpics' + str(count) + '/'):
				os.makedirs('/PATH/CREATING/JPG/OUTPUT/DIR//vidpics' + str(count) + '/')
		except OSError:
			print ('Error: Creating directory of data')
		vid = True
		while(vid):
			vid = random.choice(glob.glob('/PATH/OF/MP4/INPUT/DIR/'+'*.mp4'))
			cap = cv2.VideoCapture(vid)
				
			currentFrame = 0
			ret = True
			while(ret):
				# Capture frame-by-frame
				ret, frame = cap.read()

				# Saves image of the current frame in jpg file

				name = ('/PATH/CREATING/JPG/OUTPUT/FILE/DIR' + str(count) + '/' + str(uuid.uuid4()) + '.jpg')
				print ('Creating...' + name)
				cv2.imwrite(name, frame)
				count2 += 1

			os.remove(str(vid))
			# When everything done, release the capture
			'''
			if IndexError: Cannot choose from an empty sequence:
			print ('Your Videos Have Been Processed into Photos')
			'''
			cap.release()
			cv2.destroyAllWindows()

	except:
		pass
	count += 1




# We will now process the images created by this script in the next script, 2_ration.py

# Make a back up of the images this script created before going on to the next step.
# Compress it into a .zip file to ensure it is untouched in case you need to redo the next step
