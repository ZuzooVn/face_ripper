import glob
import uuid
import os, random
import face_recognition

root = ('/home/eagle/Aly/alvidpics/samface/alyset2/')
root2 = ('/home/eagle/Aly/alvidpics/samface/NOTaly2/')
IndexErr = ('/home/eagle/Aly/alvidpics/samface/IndexErr2/')
face = ('/home/eagle/Aly/her/aly.jpg')

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
		pic = (random.choice(glob.glob('/home/eagle/Aly/Google_Images/picset/'+'*.jpg')))
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
		print ("I don't know what to make of this. Error folder it goes!")
		os.rename(pic, IndexErr + str(uuid.uuid4()) + '.jpg')
