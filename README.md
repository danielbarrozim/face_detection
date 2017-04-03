# Face Detection Project

## Introduction

[Face detection](https://en.wikipedia.org/wiki/Face_detection) is a computer technology being used in various applications that identify human faces in digital images.  The purpose of this project is to research face detection methods and select and apply one. 

## Literature Review

Face detection is the process of identifying any human face in a given image or video. There are multiple techniques that pertain to an agent being able to detect a face in a given image. The methods are: knowledge-based, feature invariant approaches, template matching, and appearance based methods.

The knowledge-based method is a rule-based method that has encoded in it knowledge about what constitutes a human face. The researcher is the one responsible for deriving these rules. A researcher can state that a face has two eyes, a nose and mouth. The difficulty arises in translating this knowledge into rules the system can comprehend. 
In feature invariant approaches, the aim is to find features that are present in an image even when the pose, viewpoint, or lighting conditions vary. The algorithm then utilizes these features to locate faces in an image. 
Template matching method is a technique that takes multiple standard patterns of a face and computes similarities between an input image and the stored patterns. The system is then able to both locate and detect a face in an image. Template matching is very simple to implement. Yet, one of the drawbacks of this approach is that it cannot deal with variations in pose, scale, and shape. 

Finally, appearance-based methods contrast heavily with template matching such that the templates in this method are learned from receiving multiple images as data. These techniques rely on principles of machine learning and statistics to generate the “templates”. Support vector machines, hidden Markov models, and deep convolutional neural networks are all examples of appearance-based methods. 

## Theory of Histogram of Oriented Gradients

  For face detection I opted to go with the [Histogram of Oriented Gradients](http://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf) (HOG) technique. 

The HOG technique is a feature descriptor utilized in computer vision
for object detection in digital images. The principle, or theory, of histogram of oriented gradients is that objects in images can be described as the distribution of intensity gradients. HOG takes a pixel and determines which surrounding pixels are getting darker and replaces the analyzed pixel with a vector pointing towards the darkest surrounding pixel. 

![HOG applied to a face](https://www.researchgate.net/profile/Mohammad_Haghighat/publication/284243500/figure/fig5/AS:303513939791876@1449374770626/Fig-5-Histogram-of-Oriented-Gradients-HOG-features-in-4-4-cells.png)

In deciding to use this approach I compared HOG to another classic face detection technique known as Haar Cascades. I decided that while Haar Cascades may be faster and better suited for real-time applications, it provided too many false positives and HOG has better accuracy in recognizing faces. 

## Method

In order to complete this face detection project I decided to utilize the Python programming language. This was because of the many libraries available for computer vision. The primary library I utilized to implement HOG was [dlib](http://dlib.net). Students at another universities tested both HOG and Haar Cascades with both OpenCV and dlib and they found that dlib's HOG implementation was far more accurate than the others. 

In order to get dlib's Python API installed I followed PyImageSearch's instructions:
<http://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/>

