import cv2 


face_cascade = cv2.CascadeClassifier("C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")

def main():
    img=cv2.imread(r"D:\IMG_20211208_173107.jpg",cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
     
    for (x, y, w, h) in faces:
        
        faces = img[y:y + h, x:x + w]
        cv2.imshow("face",faces)
        cv2.imwrite('face.jpg',faces)
        
    cv2.imwrite('detcted.jpg', img)
    cv2.imshow('img', img)

    
    
    cv2.waitKey(1)
    cv2.destroyAllWindows()
from PIL import Image    
def main2():
    Image2 =   Image.open('face.jpg')
    Image2=Image2.resize((231,231),resample=Image.NEAREST)
    Image1=Image.open(r"D:\New folder\modi.png")
    Image1.paste(Image2,(328,67))
    Image1.show()
    
main()    
main2()