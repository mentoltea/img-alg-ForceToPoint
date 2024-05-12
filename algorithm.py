import PIL
from PIL import Image
from definitions import *
import pygame as pg

def get_pixel_at(img: Image.Image, x:int, y:int) -> Pixel:
    color = img.getpixel((x,y))
    clr = Color(color)
    return Pixel(clr, Point(x,y))

def find_center_point(img: Image.Image) -> Pixel:
    pg.init()
    (xsize, ysize) = img.size
    wn = pg.display.set_mode((xsize+10, ysize))
    pg.display.set_caption("Choose a point to filter (very important)")
    clock = pg.time.Clock()
    pimg = pg.image.fromstring(
        img.tobytes(), img.size, img.mode).convert()
    while (True):
        wn.fill((255,255,255))
        wn.blit(pimg, (0,0))
        clock.tick(14)
        
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                pg.display.quit()
                pg.quit()
                return get_pixel_at(img, xsize//2, ysize//2)
            
            if (event.type == pg.MOUSEBUTTONUP):
                if event.button == 1:
                    (x,y) = pg.mouse.get_pos()
                    pg.display.quit()
                    pg.quit()
                    return get_pixel_at(img, x, y)
        
        (x,y) = pg.mouse.get_pos()
        color = img.getpixel((x,y))
        pg.draw.rect(wn, color, (xsize, 0, 10, ysize))
        pg.display.update()
    

def alg(image: Image.Image) -> Image.Image:
    img = image.copy()
    img = img.convert("RGB")
    (xsize, ysize) = img.size
    center = find_center_point(img)
    
    templist: list[Pixel] = []
    temppix: Pixel
    for y in range(ysize):
        if (y%300==0):
            print("{0}/{1}".format(y, ysize))
        templist.clear()
        for x in range(xsize):
            temppix = get_pixel_at(img, x, y)
            templist.append(temppix)
        templist.sort(key= lambda p: p.forceTo(center))
        for x in range(xsize):
            clr = templist[x].color
            img.putpixel((x,y), tuple([clr.r, clr.g, clr.b]))
    return img        
            
        