face_recognition --cpus 8 --show-distance true ./known_people ./unknown_pictures
face_recognition --cpus 8 --show-distance true ./known_people ./test_images

face_recognition --cpus 8 --tolerance 0.4 ./known_people ./unknown_pictures
face_recognition --cpus 8 --tolerance 0.4 ./known_people ./test_images
