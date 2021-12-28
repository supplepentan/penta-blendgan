import subprocess
import gdown
import os

# フォルダ作成
os.makedirs("input")
os.makedirs("output")
os.makedirs("pretrained_models")
os.makedirs("style_imgs")

# ninjaインストール
subprocess.run(["wget", "https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip"])
subprocess.run(["sudo", "unzip", "ninja-linux.zip", "-d", "/usr/local/bin/"])
subprocess.run(["sudo", "update-alternatives", "--install", "/usr/bin/ninja ninja /usr/local/bin/ninja", "1", "--force"])
 
# 学習済みパラメータのダウンロード
gdown.download('https://drive.google.com/uc?id=1D27HPNOSx9kWIhc13VevRy0pUv_xYiJb', './pretrained_models/blendgan.pt', quiet=False)
gdown.download('https://drive.google.com/uc?id=1pWWSm_c75ieMExJPWJuYA1wby-hm4f1J', './pretrained_models/psp_encoder.pt', quiet=False)
gdown.download('https://drive.google.com/uc?id=1qshfqj8SdmgQv_kfLpiohbI3QPQF-OE5', './pretrained_models/style_encoder.pt', quiet=False)
 
# ランドマークデータのダウンロード
subprocess.run(["wget", "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"])
subprocess.run(["bzip2", "-dk", "shape_predictor_68_face_landmarks.dat.bz2"])