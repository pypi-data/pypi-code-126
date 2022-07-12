import cv2
import numpy as np
import os
import glob
import matplotlib.pyplot as plt

def get_blur_metrics(image_file, k=10):
    '''
    Calculate blur metrics by SVD (Blurred Image Region Detection and Classification, ACM Multimedia, 2011) and Laplacian.
    Blurry images have a high SVD score and low lapacian var score.

    Parameters
    ----------
    k : top k SVD eigenvalues used in SVD-based method.

    Returns
    -------
    4-element tuple : SVD-based score, blur map, laplacian variance, blur map
    '''
    img = cv2.imread(image_file,cv2.IMREAD_GRAYSCALE)
    u, s, v = np.linalg.svd(img)
    top_sv = np.sum(s[0:k])
    total_sv = np.sum(s)
    
    laplace = cv2.Laplacian(img, cv2.CV_64F)
    return top_sv/total_sv, (1 - get_blur_map(image_file) )*255, laplace.var(), cv2.convertScaleAbs(laplace)

def overlay_image(img, k = 10):
    '''
    calculate blur scores and put text anno onto the image
    '''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    u, s, v = np.linalg.svd(gray)
    top_sv = np.sum(s[0:k])
    total_sv = np.sum(s)
    
    laplace = cv2.Laplacian(gray, cv2.CV_64F)
    score1 = round(top_sv/total_sv,2)
    score2 = round(laplace.var(), 1)

    cv2.putText(img, 'SVD=' + str(score1) + ', LAPLACIAN=' + str(score2), 
    (5, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    return img

def get_blur_map(image_file, patch_size=10, k=3):

    img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    new_img = np.zeros((img.shape[0]+patch_size*2, img.shape[1]+patch_size*2))
    for i in range(new_img.shape[0]):
        for j in range(new_img.shape[1]):
            if i<patch_size:
                p = patch_size-i
            elif i>img.shape[0]+patch_size-1:
                p = img.shape[0]*2-i
            else:
                p = i-patch_size
            if j<patch_size:
                q = patch_size-j
            elif j>img.shape[1]+patch_size-1:
                q = img.shape[1]*2-j
            else:
                q = j-patch_size
            #print p,q, i, j
            new_img[i,j] = img[p,q]

    #cv2.imwrite('test.jpg', new_img)
    #cv2.imwrite('testin.jpg', img)
    blur_map = np.zeros((img.shape[0], img.shape[1]))
    max_sv = 0
    min_sv = 1
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            block = new_img[i:i+patch_size*2, j:j+patch_size*2]
            u, s, v = np.linalg.svd(block)
            top_sv = np.sum(s[:k])
            total_sv = np.sum(s)
            sv_degree = top_sv/total_sv
            if max_sv < sv_degree:
                max_sv = sv_degree
            if min_sv > sv_degree:
                min_sv = sv_degree
            blur_map[i, j] = sv_degree
    #cv2.imwrite('blurmap.jpg', (1 - blur_map) * 255)

    blur_map = (blur_map-min_sv)/(max_sv-min_sv)
    #cv2.imwrite('blurmap_norm.jpg', (1-blur_map)*255)
    return blur_map

def process_image_folder(path, save_output = False):
    '''
    path : image folder path. accept wild cards, e.g., c:/pictures/*.jpg
    '''

    rows = len(glob.glob(path))
    cols = 3
    plt.figure(figsize=(16,rows * 5))

    idx = 0
    for f in glob.glob(path): 
        
        img = cv2.imread(f, cv2.COLOR_BGR2RGB)
        score1, map1, score2, map2 = get_blur_metrics(f)

        if save_output:
            cv2.imwrite(f.replace('.jpg','_svd.jpg'), map1)
            cv2.imwrite(f.replace('.jpg','_laplacian.jpg'), map2)
        
        idx = idx+1
        plt.subplot(rows, cols, idx)
        plt.imshow(img)
        plt.axis('off')
        
        idx=idx+1
        plt.subplot(rows, cols, idx)        
        plt.imshow(map1)        
        plt.text(0, 0, round(score1, 2), color='black', bbox=dict(facecolor='white', alpha=1))
        plt.axis('off')
        
        idx=idx+1
        plt.subplot(rows, cols, idx)        
        plt.imshow(map2) 
        plt.text(0, 0, round(score2, 2), color='black', bbox=dict(facecolor='white', alpha=1))
        plt.axis('off')
        
    plt.show()
    # plt.savefig(os.path.dirname(__file__) + '/result.jpg')

if __name__ == '__main__':

    process_image_folder(os.path.dirname(__file__) + '/*.jpg', save_output=True)
