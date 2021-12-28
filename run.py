import os
import shutil
import subprocess
import cv2

#@title 画像ファイル指定
input = "02.jpg"#@param {type:"string"}
file = './align/'+input
 
# original_imagesフォルダーリセット
if os.path.isdir('test_imgs/original_imgs'):
    shutil.rmtree('test_imgs/original_imgs')
os.makedirs('test_imgs/original_imgs', exist_ok=True)
 
# original_imagesフォルダーへコピー
import shutil
shutil.copy(file, 'test_imgs/original_imgs/'+input) 

# style_transferフォルダーリセット
if os.path.isdir('results/style_transfer'):
    shutil.rmtree('results/style_transfer')
 
subprocess.run(["python", "style_transfer_folder.py", "--size", "1024", "--ckpt", "./pretrained_models/blendgan.pt", "--psp_encoder_ckpt", "./pretrained_models/psp_encoder.pt", "--style_img_path", "./test_imgs/style_imgs/", "--input_img_path", "./test_imgs/original_imgs/", "--outdir", "results/style_transfer/"])
 
# imagesフォルダーリセット
import os
import shutil
if os.path.isdir('results/images'):
    shutil.rmtree('results/images')
os.makedirs('results/images', exist_ok=True)
 
# output.mp4リセット
if os.path.exists('./results/output.mp4'):
   os.remove('./results/output.mp4')
 
# 画像のリサイズ
import cv2
import glob
files = glob.glob('results/style_transfer/*.jpg')
files.sort()
for i, file in enumerate(files):
    img = cv2.imread(file)
    img_resize = cv2.resize(img, dsize=(1536, 512))
    cv2.imwrite('results/images/'+str(i).zfill(3)+'.jpg', img_resize)
 
# 画像を動画に変換
subprocess.run(["ffmpeg", "-r", "0.6", "-i", "results/images/%3d.jpg", "-vcodec", "libx264", "-pix_fmt", "yuv420p", "results/output.mp4"])