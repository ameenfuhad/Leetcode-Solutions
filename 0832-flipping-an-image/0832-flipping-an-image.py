class Solution(object):
    def flipAndInvertImage(self, image):
        n,m=len(image),len(image[0])
        for i in range(n):
            image[i].reverse()
            for j in range(m):
                image[i][j]^=1
        return image
        