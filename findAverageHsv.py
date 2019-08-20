import cv2
import numpy as np
from openpyxl import Workbook

write_wb = Workbook()

def main(img, fileName):
    width, height, channels = img.shape
    print(fileName)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)

    count = 0
    h_sum = 0
    s_sum = 0
    v_sum = 0

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range(width):
        for j in range(height):
            if img[i,j,0] > 150:
                continue
            else:
                count = count + 1
                h_sum = h_sum + img_hsv[i, j, 0]/100000
                s_sum = s_sum + img_hsv[i, j, 1]/100000
                v_sum = v_sum + img_hsv[i, j, 2]/100000

    h = int((h_sum * 2 * 100000)/count)
    s = int(((s_sum * 100 * 100000) / 255) / count)
    v = int(((v_sum * 100 * 100000) / 255) / count)

    write_ws = write_wb.active
    write_ws['A1'] = 'h'
    write_ws['B1'] = 's'
    write_ws['C1'] = 'v'

    write_ws.append([h, s, v])


for i in range(2, 94):
    img = cv2.imread("./picture/black/origin/"+str(i)+".jpg")
    main(img, i)


write_wb.save('result_black.xlsx')

