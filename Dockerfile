FROM continuumio/miniconda3
RUN apt-get update 
RUN apt-get install -y --no-install-recommends ffmpeg

WORKDIR /usr/src/code
RUN mkdir inputs
RUN mkdir newResults
RUN pip install --no-cache-dir --upgrade pip setuptools
COPY . .
RUN conda create -n videocrafter python=3.8 -y
RUN conda run -n videocrafter
RUN pip --version
RUN pip install --no-cache-dir -r requirements_1.txt
RUN pip install --no-cache-dir eva-decord==0.6.1
RUN pip install --no-cache-dir -r requirements_2.txt






