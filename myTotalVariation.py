import os
from skimage import img_as_float
from matplotlib import pyplot as plt
from skimage import io
from skimage.restoration import denoise_tv_chambolle

Input_Folder = './JPG_IMAGES/'
Output_Folder = './TV_IMAGES/'

Input_Image_List = os.listdir(Input_Folder)

if os.path.isdir(Output_Folder) is False:
    os.mkdir(Output_Folder)

for i in range(0, len(Input_Image_List)):
    noisy_img = img_as_float(io.imread(Input_Folder + Input_Image_List[i]))
    Output_Image = denoise_tv_chambolle(noisy_img, weight=0.3, multichannel=False)
    plt.imsave(Output_Folder + str(i+1) + '.png', Output_Image, cmap='gray')
    # plt.imshow(Output_Image, cmap='gray')
    # plt.show()