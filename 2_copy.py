'''
Now that we have each video's frames converted to jpgs and in their own folders we will take an equal,
random sampling of 500 frames from each folder. This ensures that every type of angle and lighting on
each face gets an equal representation in our final dataset in spite of any video length.

Of course your individual photo files of each videos will likely have upwards of 5000 photos each, we
will only select 500 randomly from each for efficiency's sake. This will make sense later and you should
have a healthy faceset by the time the process is over, dispite leaving photos of the face behind.
The '500' number is adjustable. You may need more. You may want less from each video AND more videos.

The input images this script uses are the images output by the last script, 1_vids_to_pics.py
The output images this script creates are the input images in the next script, 3_one_face.py
'''
import glob
import uuid
import os, random
from shutil import copyfile

try:
	if not os.path.exists('/home/eagle/Aly/_0_0_0_kaylee/sampled'):
		os.makedirs('/home/eagle/Aly/_0_0_0_kaylee/sampled')
except OSError:
	print ('Error: Creating directory of data')

count1 = 1
count2 = 4
for i in range(1):
	for i in range(3000):
		one = random.choice(glob.glob('/home/eagle/Aly/_0_0_0_kaylee/vidpics'+str(count2)+'/'+'*.jpg'))
		two = '/home/eagle/Aly/_0_0_0_kaylee/sampled/' + str(count1) + '-' + str(uuid.uuid4()) + '.jpg'

		os.rename(one, two)

		print (one)

		count1 += 1
	count2 += 1



























