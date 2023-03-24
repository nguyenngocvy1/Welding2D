import numpy as np
import cv2
from win32api import GetSystemMetrics
from pprint import pprint


def remove_shadows(img):
    rgb_planes = cv2.split(img)
    result_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        result_planes.append(diff_img)
        result = cv2.merge(result_planes)
        return result

def connect_broken_lines(img):
    kernel = np.ones((20,20), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    return img

def remove_background(img_th):
    h, w = img_th.shape[:2] # notice the size needs to be 2 pixels than the image.
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(img_th, mask, (0,0), 255) # floodfill from point (0, 0)
    img_th = cv2.bitwise_not(img_th) # invert foolfilled image
    return img_th

def write_cloud_points(text, file_name):
    f = open(file_name,'w')
    f.write(text)
    f.close()

def show(img_name, img):
    screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)
    img_resize = cv2.resize(img,(screen_width,screen_height),interpolation=cv2.INTER_LINEAR)
    cv2.imshow(img_name,img_resize)
    
 
if __name__ == '__main__':
    img = cv2.imread('test6.jpg')
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img,9)
    img_gray = remove_shadows(img_gray)
    show('gray',img_gray)

    _, img_th = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    show('th',img_th)
    img_th = cv2.bitwise_not(img_th)
    img_th = connect_broken_lines(img_th)
    img_th = remove_background(img_th)
    show('bg',img_th)
    # img_th = cv2.ximgproc.thinning(img_th)

    contours, _ = cv2.findContours(img_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    text = ""
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.0009 * cv2.arcLength(contour, True), True)
        contour_list = approx.ravel()
        for i in range(0,len(contour_list)):
                if i % 2 == 0:
                    x = contour_list[i]
                    y = contour_list[i+1]
                    cloud_points = '{}\t{}\t0\n'.format(x,y)
                    text += cloud_points
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 4)
        write_cloud_points(text, 'cloud_points{}.txt'.format(count))
        count += 1

    show('img',img)
    # cv2.imwrite('result11.png',img)
    cv2.waitKey(0)

