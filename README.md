# face_ripper
This proportionally grabs video frames from batches of mp4 videos and builds a faceset of your desired face.
By the time you have run all these scripts you should be left with a folder containing thousands of photos.
Each photo in this folder will be a picture with exactly one face.
They face in each photo will be face of the specific person you wanted extraced from your mp4 videos.

These scripts should be used in numerical order.
Each script's output is the next script's input.
It's a good idea to make a backup, zip copy of every script's output before proceeding to the next one.

Play with the scripts with directories containing small amounts of jpgs at first so you make sure everything
is grabbing and putting everything to, and from where you want.

# Dependancies
These scripts are dependant on the face_recognition app by ageitgey here https://github.com/ageitgey/face_recognition

All dependancies required to run that are the depancies needed to be installed to run this.

If you have a GPU you should set up dlib in order to use your GPU
