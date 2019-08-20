import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import scipy.misc


read_dir = "./picture/black/removedBG/"
write_dir = "./picture/black/result/"

def main(filename):
    img = cv2.imread(read_dir+filename+".jpg", cv2.IMREAD_COLOR)
    print(filename)

    # width, height, channels = img.shape
    # crop_img = img[0:height, 0:width]

    blur = cv2.bilateralFilter(img, 9, 75, 75)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 2)
    contours, h = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # max_size = 0
    # max_contour = None
    # for i in contours:
    #     if cv2.contourArea(i) > max_size:
    #         max_contour = i
    #
    # (x, y, w, h) = cv2.boundingRect(max_contour)
    #
    # if w > h:
    #     h = w
    # else:
    #     w = h

    width, height, channels = img.shape

    # find mask. this code don't use
    # mask_img = np.zeros(shape=[width, height, channels], dtype=np.uint8)

    # for i in range(0, width):
    #     for j in range(0, height):
    #         if i > x-30 and i < x+w+30:
    #             if j > y-30 and j < y+h+30:
    #                 mask_img[j, i] = [169, 169, 169]
    #
    # cv2.drawContours(mask_img, contours, -1, (255, 255, 255), 3)
    #
    # cv2.imwrite("./picture/mask.jpg", mask_img)

    # img = cv2.imread(read_dir + filename + ".jpg", cv2.IMREAD_COLOR)
    mask = np.zeros(img.shape[:2], np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    rect = (1, 1, width, height)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    crop_img = img * mask2[:, :, np.newaxis]

    # use mask - this codes accuracy is not good. need to modify
    # cv2.imshow("img", img)
    # mask = np.zeros(img.shape[:2], np.uint8)
    #
    # bgdModel = np.zeros((1, 65), np.float64)
    # fgdModel = np.zeros((1, 65), np.float64)
    #
    # # Step 1
    # rect = (x, y, x + w, y + h)
    # cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)
    #
    # # Step 2
    # newmask = cv2.imread('./picture/mask.jpg', 0)
    #
    # mask[newmask == 0] = 0
    # mask[newmask == 255] = 1
    # cv2.grabCut(img, mask, None, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_MASK)
    #
    # mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    # img = img * mask2[:, :, np.newaxis]

    # im = Image.fromarray(img, 'RGB')
    # result_img = cv2.cvtColor(img, cv2.COLOR_YCR_CB2BGR)
    # cv2.imwrite("./picture/result2.png", result_img)
    # plt.imshow(img), plt.show()

    crop_img_rgb = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
    plt.imsave(write_dir+filename+".jpg", crop_img)

for i in range(2, 93):
    main(str(i))
    print(i)



