import cv2  
import numpy as np  
from PIL import Image

def search(image, temp):
    if type(image) == type(""):
        img_rgb = cv2.imread(image,1)
    else:
        img_rgb = image
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  
    template = cv2.imread(temp,0)  
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)   
    threshold = 0.8  
    loc = np.where( res >= threshold) 
    return img_rgb, loc  # 


def color_pixel(kletki, img, color):
    for key in kletki:
        sum_r, sum_g, sum_b = 0,0,0
        for i in range(0,50,2):
            for j in range(0,50,2):
                x, y = kletki[key]
                r, g, b = img.getpixel((x + i, y + j))
                sum_r += r
                sum_g += g
                sum_b += b
        color[key] = round((sum_r / 25) + (sum_g / 25) + (sum_b / 30))
    return color


image = r'C:\\Users\\danil\\Desktop\\chess\\main\\images\\board.jpg'
# temp = r'RightUpB.jpg'
img_rgb, loc = search(image, 'C:\\Users\\danil\\Desktop\\chess\\main\\images\\template_edge.jpg') #
os_y = list()
os_x = list()
for pt in zip(*loc[::-1]):
    os_x.append(pt[0])
    os_y.append(pt[1])
x_min, y_min =  min(os_x) + 66, min(os_y) + 64
x_max, y_max =  max(os_x), max(os_y)
kletki = dict()
color = dict()
cords = list()
step_v = int((y_max - y_min) / 8)  
step_g = int((x_max - x_min) / 8)  
letter = ['A','B','C','D','E','F','G','H']
# letter = ['H','G','F','E','D','C','B','A']
for i in range(y_min,y_max-step_v, step_v):
    for j in range(x_min,x_max-step_g,step_g):
        img_rgb[i][j] = (0,0,255)
        cord = j ,i
        cords.append(cord)
chet = 0
for i in range(1,9):
    for j in letter:
        mark = j + str(i)
        kletki[mark] = cords[chet]
        color[mark] = ''
        chet += 1
    
img = Image.open(image)
color = color_pixel(kletki, img, color)
print(color)



# for i in letter:
#     key = i + '7'
#     print(color[key])

cv2.imwrite('res.png', img_rgb)