import numpy as np
import cv2 as cv

def undistortLeft(img,mtx,dist):
    h,w = img.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h),1, (w,h))  
    dst = np.array([])
    dst = cv.undistort(img, mtx, dist, dst, mtx)
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    #cv.imwrite('undistortImageLeft.jpg',dst)
    #cv.imshow('result',dst)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    return dst
    

def undistortRight(img,mtx,dist):
    h,w = img.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h),1, (w,h))
    dst = np.array([])
    dst = cv.undistort(img, mtx, dist, dst, mtx)
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    #cv.imwrite('undistortImageRight.jpg',dst)
    #cv.imshow('result',dst)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    return dst
