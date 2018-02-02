'''
Now that we have a dir of photos that all contain ONE face we will get this script to remove photos of
faces belonging to people other than your target.

This script will look at ONE photo you provide to this script, recognize the face in your set of photos,
and sort the photos of the desired face into a folder.

There are FIVE different directories involded in this scrpit.
Location 1 - A passport style photo of the face you desired for the face_recognition module to learn (path to jpg file)
Location 2 - Your directory from the last script that contains photos of ONE face in all
Location 3 - A new directory you specify for this script to place the photos of your target face
Location 4 - A new directory you specify for this script to place the photos that are NOT of your target face
Location 5 - A new directory this script will through photos this script has a problem with for some reason
It's a good idea to move all of these photos back into location 2 (this scripts input images)
THEN change your learned, passport style import image (Location 1) to a photo of the face at another angle
'''

import glob
import uuid
import os, random
import face_recognition

root = ('<DIR FOR Location 3>')
root2 = ('<DIR FOR Location 4>')
IndexErr = ('<DIR FOR Location 5>')
face = ('<PATH TO FILE AT Location 1>')

#Create directories for sorted photos
try:
	if not os.path.exists(root):
		os.makedirs(root)
except OSError:
	print ('Error: Creating directory of data')

try:
	if not os.path.exists(root2):
		os.makedirs(root2)
except OSError:
	print ('Error: Creating directory of data')

try:
	if not os.path.exists(IndexErr):
		os.makedirs(IndexErr)
except OSError:
	print ('Error: Creating directory of data')

picture_of_me = face_recognition.load_image_file(face)
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
for i in range(1000):
	try:
		pic = (random.choice(glob.glob('<Location 2> /PATH/OF/JPG/INPUT/DIRS/'+'*.jpg')))
		print (pic)
		unknown_picture = face_recognition.load_image_file(pic)
		unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

		# Now we can see the two face encodings are of the same person with `compare_faces`!

		results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

		if results[0] == True:
			print("It's a picture of our girl!")
			os.rename(pic, root + str(uuid.uuid4()) + '.jpg')
		else:
			print("It's not a picture of our girl")
			os.rename(pic, root2 + str(uuid.uuid4()) + '.jpg')
	except IndexError:
		print ("I don't know what to make of this. Error folder it goes! Look at it later!")
		os.rename(pic, IndexErr + str(uuid.uuid4()) + '.jpg')
