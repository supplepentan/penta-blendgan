# Usage
```
git clone https://github.com/supplepentan/penta-blendgan.git
cd penta-blendgan
wsl
pyenv local 3.8.6
python -m venv venv-wsl
source venv-wsl/bin/activate
python -m venv venv-wsl
source venv-wsl/scripts/activate
python -m pip install -r requirements.txt
python -m pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
python setup.py
python run.py

```
# style_imgs
https://drive.google.com/u/0/uc?id=1uOYaBR_LUN4zml9QUmdc5wECjGnSw_-s&export=download

# Original
https://onion-liu.github.io/BlendGAN/