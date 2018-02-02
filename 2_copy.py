'''
Now that we have each video's frames converted to jpgs and in their own folders we will take an equal,
random sampling of 3000 frames from each folder. This ensures that every type of angle and lighting on
each face gets an equal representation in our final dataset in spite of any video length.

Of course your individual photo files of each videos will likely have upwards of 5000 photos each, we
will only select 3000 randomly from each for efficiency's sake. This will make sense later and you should
have a healthy faceset by the time the process is over, dispite leaving photos of the face behind.
The '3000' number is adjustable. You may need more. You may want less from each video AND more videos.

The input images this script uses are the images output by the last script, 1_vids_to_pics.py
The output images this script creates are the input images in the next script, 3_one_face.py
'''
import glob
import uuid
import os, random
from shutil import copyfile

try:
	if not os.path.exists('/PATH/CREATING/JPG/OUTPUT/FILE/DIR/sampled/'):
		os.makedirs('/PATH/CREATING/JPG/OUTPUT/FILE/DIR/sampled/')
except OSError:
	print ('Error: Creating directory of data')

count1 = 1
count2 = 4
#This begins working on your video file's individual photo files.
#The range number below should be the number of videos you started with
for i in range(10):
	#This range number is the number of photos you want from each jpg-ed videos
	#If one of your video has a bigger range of shaddows, emotions, and agles you should modify this
	#...script to grab a higher number of jpgs from that jpg-ed folder with another pass
	for i in range(3000):
		#The last python script numbered photo's video's into their own, numbered dirs
		#Make this line find and do their work on these numbered dirs
		one = random.choice(glob.glob('/PATH/OF/MP3/INPUT/DIRS/'+str(count2)+'/'+'*.jpg'))
		
		#This pu
		two = '/PATH/CREATING/JPG/OUTPUT/FILE/DIR/sampled/' + str(uuid.uuid4()) + '.jpg'

		os.rename(one, two)

		print (one)

		count1 += 1
	count2 += 1



























