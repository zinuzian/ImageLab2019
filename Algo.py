import numpy as np
import matplotlib.pyplot as plt

from skimage import measure, io, restoration
import os


class ContourFinder:

    def __init__(self, filepath):
        '''

        :param filepath: absolute path of the file
        '''

        # Check if necessary directories exist
        dirCheckList = ['images','images/temp']
        for directory in dirCheckList:
            if not os.path.isdir(directory):
                os.mkdir(directory)

        # Load img file
        self.filepath = filepath
        self.image = io.imread(self.filepath, as_grey=True)
        self.color = "#FFFFFF"

    def setColor(self, colorValue):
        self.color = colorValue

    def choose(self):
        pass

    def find(self, value):
        # Denoise the original image
        denoised = restoration.denoise_tv_chambolle(self.image, weight=0.1, multichannel=True)
        # denoised = restoration.denoise_wavelet(self.image, multichannel=True)
        # Find contours at a constant value
        # Uses Marching Squares Algorithm
        contours = measure.find_contours(denoised, value)

        # Display the image and plot all contours found
        fig, ax = plt.subplots(figsize=(20, 20))
        ax.imshow(self.image, cmap=plt.cm.gray)
        # ax.imshow(denoised, cmap=plt.cm.gray)

        for n, contour in enumerate(contours):
            ax.plot(contour[:, 1], contour[:, 0], linewidth=2, color=self.color)


        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.savefig('images/result.png', bbox_inches='tight', pad_inches=0, dpi=100)
        # plt.show()

        return 'images/result.png'

if __name__ == "__main__":
    filepath = "./images/test.png"
    cf = ContourFinder(filepath)
    cf.find(0.5)



