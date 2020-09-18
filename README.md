Categorize Dinasour
====

Overview

- Deep learning for categorizing dinasour
- keras + tensorflow

## Requirement

- python 3.6.9
- tensorflow-gpu 1.14.0
- keras 2.3.1

## Usage

1. Download image  
search images with the following keywords using Google, then download the images.

- tyrannosaurus
- triceratops
- brachiosaurus
- stegosaurus
- iguanodon
- ornithomimus
- pteranodon

2. Store and resize images  
place the images to the following directory, then start images/resize_image.py

- images/tyrannosaurus
- images/triceratops
- images/brachiosaurus
- images/stegosaurus
- images/iguanodon
- images/ornithomimus
- images/pteranodon

3. Configurate image and lable  
compile and execute configurate.cpp to create following files:

- data/trainImage256_300_shuffle.txt
- data/trainImage256_300.txt
- data/trainImage256_100_shuffle.txt
- data/trainImage256_100.txt
- data/testImage256_shuffle.txt
- data/testImage256.txt

**If you have troublesome in the procedures above, please download the files from:**

4. Build library  
To build library, operate as:

```
mkdir build
cd build
cmake ..
make
cd ..
cp build/*.so ./
```

5. Check data  
start check_data.py

6. Training with tensorflow  
start as: 

```
bash train.sh
```

7. Inference  
start apply_model.py  

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)