import numpy as np
import cv2
import grabcut

read_dir = "./picture/black/left/"
read_dir2 = "./picture/black_left/"
write_dir = "./picture/black_result/left/"

def main(fileName):
    img = cv2.imread(read_dir2+fileName+'.jpg', cv2.IMREAD_COLOR)
    img_origin = cv2.imread(read_dir+fileName+".jpg", cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, thr = cv2.threshold(gray, 10, 255, 0)

    contours, heirachy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    max_size = 0
    max_contour = None
    for i in contours:
        if cv2.contourArea(i) > max_size:
            max_size = cv2.contourArea(i)
            max_contour = i

    x, y, w, h = cv2.boundingRect(max_contour)
    middle_x = int((x+x+w)/2)
    middle_y = int((y+y+h)/2)
    point1_x = int((x + x + middle_x)/3)
    point2_x = int((x + w + x + w + middle_x)/3)

    img_hsv = cv2.cvtColor(img_origin, cv2.COLOR_BGR2HSV)
    cv2.drawContours(img_origin, max_contour, -1, (0, 255, 255), 2)
    cv2.circle(img_origin, (point1_x, middle_y), 3, (0, 0, 255), 5)
    cv2.circle(img_origin, (point2_x, middle_y), 3, (0, 255, 0), 5)
    cv2.imshow("img_origin", img_origin)
    cv2.waitKey(0)
    print(img_origin[middle_y, middle_x])
    h1 = img_hsv[middle_y, point1_x][0]*2
    s1 = (img_hsv[middle_y, point1_x][1]*100)/255
    v1 = (img_hsv[middle_y, point1_x][2]*100)/255

    h2 = img_hsv[middle_y, point2_x][0] * 2
    s2 = (img_hsv[middle_y, point2_x][1] * 100) / 255
    v2 = (img_hsv[middle_y, point2_x][2] * 100) / 255

    # print(int(h))
    # print(int(s))
    # print(int(v))

    return h1, s1, v1, h2, s2, v2
    cv2.imshow("img", img)
    cv2.imshow("origin", img_origin)
    cv2.waitKey(0)

