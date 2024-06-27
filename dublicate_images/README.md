# Image Duplicate Finder
Finds duplicates of images.

## Table of Contents
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Running](#running)
- [About The Project](#about-the-project)


## Technologies
- [PIL](https://pypi.org/project/pillow/)
- [matplotlib](https://matplotlib.org/)
- [imagehash](https://pypi.org/project/ImageHash/)
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

## Getting Started

### Installation
You should install additional libraries like:
- PIL
- matplotlib
- imagehash
Using following command:
```
pip install requirements.txt
```

### Preparation
- Put a folder with your images in the folder of project(where main.py file is situated)
- Change name(s) of folder(s) in main.py:
```
folders = [
        os.path.join("5 Flower Types Classification Dataset", "Lilly"),
        os.path.join("5 Flower Types Classification Dataset", "Lotus"),
        os.path.join("5 Flower Types Classification Dataset", "Orchid"),
        os.path.join("5 Flower Types Classification Dataset", "Sunflower"),
    ]
```


## Running
You should be in the folder of this project. So, just run this command:
```
python main.py
```


## About The Project
This program allows you to find duplicates of images using imagehash.
