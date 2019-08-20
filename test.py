import cv2

def main(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    cv2.waitKey(0)

    ret, thr = cv2.threshold(gray, 100, 150, cv2.THRESH_BINARY)

    contours, h = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(thr, contours, -1, (255, 0, 0), 3)

    cv2.imshow("img", thr)
    cv2.waitKey(0)


for i in range(2, 94):
    path = "./picture/black/removedBG/"+str(i)+".jpg"
    main(path)