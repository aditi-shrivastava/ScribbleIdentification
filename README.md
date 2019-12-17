# Scribble Identification

Models - CNN, MLP, GAN

This project aims at predicting scribbles from canvas and also using GAN generated images.

Idea was inspired from Kaggle's competition - https://www.kaggle.com/c/quickdraw-doodle-recognition/overview


# Contributors

* Aditi Shrivastava
* Akash S Kunwar
* Rohan Harode
* Shubham Malik


# Overview - 
1. Trained a GAN model on few categories of objects from Quick Draw dataset. Save generated images in directory.(scribblegan.py)
2. Built a training model using a ConvNet and MLP Model (train.py).
3. Developed prediction model (server.py) which takes input from either canvas or GAN category dropdown (use saved images).


# Tech Stack - 
1. ML Libraries - Tensorflow, Keras, Scipy, Python
2. Webapp - Electron JS, HTML, JQuery and Flask App. 

NOTE: This project works in Tensorflow 2.x with v1 compatibility.


Few images from WebApp and model - 

# Webapp - 

![WebApp](https://github.com/rohanharode/Scribble-Prediction-CNN-GAN/blob/master/static/webapp.png)


# GAN samples -

![GAN-Sample](https://github.com/darklord0794/Scribble-Prediction-CNN-GAN-/blob/master/gan-final_chart.png)


# GAN Loss - 

![GAN-Loss](https://github.com/darklord0794/Scribble-Prediction-CNN-GAN-/blob/master/gan-loss.png)


