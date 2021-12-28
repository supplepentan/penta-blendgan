#@title 顔画像の切り出し
import os
import shutil
from tqdm import tqdm
import glob
import subprocess

def run_alignment(image_path):
  import dlib
  from alignment import align_face
  predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
  aligned_image = align_face(filepath=image_path, predictor=predictor) 
  return aligned_image 

files = glob.glob("./input/*.jpg") #元になる画像
print(files)
for i, file in enumerate(tqdm(files)):
  basename = os.path.splitext(os.path.basename(file))[0]
  basename_ex = os.path.basename(file)
  img_dir = os.path.join("output", basename)
  img_face = os.path.join("output", basename, "face_{0}.jpg".format(basename))
  print(img_face)
  if not os.path.exists(img_dir):
    os.mkdir(img_dir)
  if file=='.ipynb_checkpoints':
     continue
  input_image = run_alignment(file)
  input_image.resize((1024,1024))
  input_image.save(img_face)
  subprocess.run(["python", "style_transfer_folder.py", "--size", "1024", "--ckpt", "./pretrained_models/blendgan.pt", "--psp_encoder_ckpt", "./pretrained_models/psp_encoder.pt", "--style_img_path", "./style_imgs/", "--input_img_path", img_dir, "--outdir", os.path.join(img_dir, "style_transfer")])