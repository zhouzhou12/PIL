'''
将图像转换为NumPy数组,并进行颜色通道互换和灰度变换
'''
from PIL import Image
import numpy as np
import pylab

im=Image.open('test.jpg')

#图像转换为numpy数组
im1=np.array(im)
print(im1.shape,im1.dtype)

#图像红色通道和蓝色通道互换
r=im1[:,:,0]
im1[:,:,0]=im1[:,:,2]
im1[:,:,2]=r
pylab.imshow(im1)
pylab.show()

#灰度化,转换为数组,数据类型转为浮点型.
im2=np.array(im.convert('L'),'f')
print(im2.shape,im2.dtype)
pylab.imshow(im2)
#pylab.show()

#灰度变换
im3=255.0-im2 #反相处理
im4=100+(100.0/255)*im2*100.0 #像素转换到100~200
im5=255.0*(im2/255.0)**2  #二次函数变换
pylab.subplot(221)
pylab.title('f(x)=x')
pylab.gray()
pylab.imshow(im2)
pylab.subplot(222)
pylab.title('f(x)=255-x')
pylab.gray()
pylab.imshow(im3)
pylab.subplot(223)
pylab.title('f(x)=100+(100/255)*im2*100')
pylab.gray()
pylab.imshow(im4)
pylab.subplot(224)
pylab.title('f(x)=255*(im2/255)^2')
pylab.gray()
pylab.imshow(im5)
pylab.show()

