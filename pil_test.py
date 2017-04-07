from PIL import Image

im=Image.open('test.jpg')
print(im.format,im.size,im.mode)
im.show()

box=(100,100,200,200)
region=im.crop(box)
region.show()
region=region.transpose(Image.ROTATE_180)
region.show()
im.paste(region,box)
im.show()

def roll(image,delta):
    #Roll an image
    xsize,ysize=image.size
    delta=delta % xsize
    if delta==0:
        return image
    part1=image.crop((0,0,delta,ysize))
    part2=image.crop((delta,0,xsize,ysize))
    image.paste(part1,(xsize-delta,0,xsize,ysize))
    image.paste(part2,(0,0,xsize-delta,ysize))
    return image

im1=roll(im,100)

out=im.resize((150,120))
out.show()
out=im.rotate(45)
out.show()
