import numpy as np
import matplotlib.pyplot as plt

from skimage import measure, io, restoration, color, img_as_ubyte
import os
from PyQt5 import QtGui, QtCore, QtWidgets
from skimage.draw import line, set_color



class ContourFinder:

    def __init__(self, filepath):
        '''

        :param filepath: absolute path of the file
        '''

        # Check if necessary directories exist
        dirCheckList = ['images', 'images/temp']
        for directory in dirCheckList:
            if not os.path.isdir(directory):
                os.mkdir(directory)

        # Load img file
        self.filepath = filepath
        self.grayPath = "images/temp/gray.png"
        self.resultPath = "images/temp/result.png"
        self.original = io.imread(self.filepath, as_gray=True)
        # io.imsave(self.grayPath, self.original)
        # print(self.original.shape)
        self.pen_color = "#ff0000"
        self.value = -1.0


    def getQImg(self):
        qimage = QtGui.QImage(self.grayPath) # grayscale image
        qimage = QtGui.QImage(self.filepath) # original image
        return qimage

    def setColor(self, colorValue):
        self.color = colorValue

    def choose(self, x, y):
        self.value = self.original[y][x]
        return self.value


    def find(self, value):
        try:
            # Denoise the original image
            denoised = restoration.denoise_tv_chambolle(self.original, weight=0.1, multichannel=True)
            # denoised = restoration.denoise_wavelet(self.image, multichannel=True)

            # Find contours at a constant value
            # Uses Marching Squares Algorithm
            contours = measure.find_contours(denoised, value)

            return contours

        except Exception as e:
            print(e)

    def save(self, savePath, contours, colorStr):
        try:
            h = colorStr.lstrip('#')
            colorIntArray = list(int(h[i:i + 2], 16) for i in (0, 2, 4))
            colorIntArray = np.array(colorIntArray)

            colorFloatArray = colorIntArray

            ext = self.filepath.split('.')[1]
            if ext == "png" or ext == "PNG":
                print("png detected")
                # colorIntArray = np.append(colorIntArray, [1])
                colorFloatArray = np.append(colorFloatArray, [255])


            # print(colorIntArray)
            print(colorFloatArray)

            temp = io.imread(self.filepath, as_gray=False)
            print(temp)
            for n, contour in enumerate(contours):
                for i in range(len(contour) - 1):
                    rr, cc = line(int(contour[i, 0]), int(contour[i, 1]), int(contour[i + 1, 0]),
                                  int(contour[i + 1, 1]))
                    # set_color(temp, (rr, cc), colorIntArray)
                    set_color(temp, (rr, cc), colorFloatArray)

            print(temp)
            io.imsave(savePath, temp)

            return True
        except Exception as e:
            print(e)




if __name__ == "__main__":
    filepath = "images/test.png"
    cf = ContourFinder(filepath)

    cf.save("images/result.png", cf.find(0.5), "#ff0000")



