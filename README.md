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

# Docker
```
docker build -t penta-blendgan .
docker run --name penta-blendgan -it --gpus all -t penta-blendgan:latest
```

# Original
https://onion-liu.github.io/BlendGAN/