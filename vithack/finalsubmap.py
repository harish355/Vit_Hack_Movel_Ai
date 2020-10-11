import cv2
import numpy as np
import time
import pyautogui
c=0



def find_rooms(imga, noise_removal_threshold=75, corners_threshold=0.1,
               room_closing_max_length=100, gap_in_wall_threshold=500):
    assert 0 <= corners_threshold <= 1
    
    imga[imga < 128] = 0
    imga[imga > 128] = 255
    _, contours, _ = cv2.findContours(~imga, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(imga)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > noise_removal_threshold:
            cv2.fillPoly(mask, [contour], 255)

    imga = ~mask
    dst = cv2.cornerHarris(imga ,2,3,0.04)
    dst = cv2.dilate(dst,None)
    corners = dst > corners_threshold * dst.max()

    for y,row in enumerate(corners):
        x_same_y = np.argwhere(row)
        for x1, x2 in zip(x_same_y[:-1], x_same_y[1:]):

            if x2[0] - x1[0] < room_closing_max_length:
                color = 0
                cv2.line(imga, (x1, y), (x2, y), color, 1)

    for x,col in enumerate(corners.T):
        y_same_x = np.argwhere(col)
        for y1, y2 in zip(y_same_x[:-1], y_same_x[1:]):
            if y2[0] - y1[0] < room_closing_max_length:
                color = 0
                cv2.line(imga, (x, y1), (x, y2), color, 1)


    _, contours, _ = cv2.findContours(~imga, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    mask = np.zeros_like(mask)
    cv2.fillPoly(mask, [biggest_contour], 255)
    imga[mask == 0] = 0

    ret, labels = cv2.connectedComponents(imga)
    imga = cv2.cvtColor(imga,cv2.COLOR_GRAY2RGB)
    unique = np.unique(labels)
    rooms = []
    for label in unique:
        component = labels == label
        if imga[component].sum() == 0 or np.count_nonzero(component) < gap_in_wall_threshold:
            color = 0
        else:
            rooms.append(component)
            color = np.random.randint(0, 255, size=3)
        imga[component] = color

    return rooms, imga




def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]
        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower =  np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
        image=cv2.imread("/home/mrstark/vithack/z.pgm")
        image_mask = cv2.inRange(image_hsv,lower,upper)
        image_mask= cv2.cvtColor(image_mask,cv2.COLOR_GRAY2RGB)
        selected_area = cv2.bitwise_and(image_mask,image, mask = None) 
        selected_area = cv2.circle(selected_area, (x,y), 2, [0,0,255], 2)
        cv2.imshow("selected_region",selected_area)
        cv2.waitKey(1000)
        name_image=raw_input("enter the name of the selected region : ")
        cv2.imwrite("submap/"+name_image+".png",selected_area)
        if len(name_image)>0:
            cv2.destroyAllWindows()
            main()


def main():
    import sys
    global image_hsv, pixel
    image_src=cv2.imread("/home/mrstark/vithack/result.png")
    image_src=cv2.GaussianBlur(image_src,(3,3),0)
    if image_src is None:
        print ("the image read is None............")
        return
    cv2.namedWindow('hsv')
    cv2.setMouseCallback('hsv', pick_color)

    image_hsv = cv2.cvtColor(image_src,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",image_hsv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    imga = cv2.imread("/home/mrstark/vithack/z.pgm", 0)
    imga = cv2.blur(imga, (2,2)) 

    rooms, colored_house = find_rooms(imga.copy())

    cv2.imwrite("result.png",colored_house)

    main()