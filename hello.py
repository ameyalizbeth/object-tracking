import cv2

img = cv2.imread('chessboard.png',1)
print("width",img.shape[1])
print("height",img.shape[0])
#scale_percent = 10 # percent of original size

#width = int(img.shape[1] * scale_percent / 100)

#height = int(img.shape[0] * scale_percent / 100)

#dim = (width, height)
# resize image
#resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
width=img.shape[1]
height=img.shape[0]
cv2.rectangle(img,(int(3*width/8),int(3*height/8)) ,(int(5*width/8),int(5*height/8)),(0,0,255), 4)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()