from deepface import DeepFace

models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
metrics = ["cosine", "euclidean", "euclidean_l2"]

df = DeepFace.find(img_path = "alumnos/PAZ.jpg",db_path= "my_db/", enforce_detection="true")

df = DeepFace.find(img_path = "profesores/MGMT.jpg",db_path= "my_db/", enforce_detection="true")

print ("Resultado ")
print (df)
