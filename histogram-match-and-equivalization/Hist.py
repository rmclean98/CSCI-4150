import numpy as np

class Hist:

    #gets the histogram from a flatten np array
    def get_histogram(image, bins):
        hist = np.zeros(bins)

        for p in image:
            hist[p] += 1

        return hist

    #Gets cumilative sum of the flatten np array
    def sum(a):
        a = iter(a)
        b = [next(a)]
        for i in a:
            b.append(b[-1] + i)
        return Hist.normalize(np.array(b))

    #normalizes the cumilative sum data
    def normalize(img):
        nj = (img - img.min()) * 255
        N = img.max() - img.min()

        img = nj / N
        img = img.astype('uint8')

        return img
