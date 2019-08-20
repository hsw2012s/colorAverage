import cv2

read_dir = './picture/black/origin/'
write_dir1 = './picture/black/left/'
write_dir2 = './picture/black/right/'

def main(fileName):
    img = cv2.imread(read_dir + fileName + ".jpg", cv2.IMREAD_COLOR)
    print(fileName)

    width, height, channels = img.shape
    crop_img = img[0:height, 0:width]
    cv2.imwrite(write_dir1+fileName+'.jpg', crop_img)

    crop_img = img[0:height, width:width*2]
    cv2.imwrite(write_dir2+fileName+'.jpg', crop_img)

for i in range(2, 93):
    main(str(i))
    print(i)
