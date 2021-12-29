FROM lapidarioz/python3-opencv3-dlib-cuda

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -U --no-cache-dir -r requirements.txt
RUN pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html