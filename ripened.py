import cv2

cv2.namedWindow('riped', cv2.WINDOW_NORMAL)
cv2.namedWindow('unriped', cv2.WINDOW_NORMAL)

frame1 = cv2.imread("sample1.png")
frame2 = frame1
frame3 = cv2.imread("sample2.png")

compare1 = cv2.compare(frame1,frame2,0)
compare2 = cv2.compare(frame1,frame3,0)

cv2.imshow('riped', compare1)
cv2.imshow('unriped', compare2)

if compare1.all():
    print "ready to plug the mango"
else:
    print "it is unripened"

if compare2.all():
    print "ready to plug the mango"
else:
    print "it is unripened"

cv2.waitKey(0)
cv2.destroyAllWindows()