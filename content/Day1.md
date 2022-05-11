# การติดตั้งสภาพแวดล้อมสำหรับการพัฒนาโค้ด

ก่อนที่เราจะเริ่มสร้างแอป Streamlit ได้ เราจะเริ่มต้นด้วยการติดตั้งสภาพแวดล้อม conda สำหรับการเขียนโค้ด

## **การติดตั้ง conda**
- Install `conda` by going to https://docs.conda.io/en/latest/miniconda.html and choose your operating system (Windows, Mac or Linux). 
- Download and run the installer to install `conda`.

## **การสร้างสภาพแวดล้อม conda ใหม่**
Now that you have conda installed, let's create a conda environment for managing all the Python library dependencies.

To create a new environment with Python 3.9, enter the following:
```bash
conda create -n stenv python=3.9
```

where `create -n stenv` will create a conda environment named `stenv` and `python=3.9` will setup the conda environment with Python version 3.9.

## **การเริ่มใช้งานสภาพแวดล้อม conda**

To use a conda environment that we had just created that is named `stenv`, enter the following into the command line:

```bash
conda activate stenv
```

## **การติดตั้ง Streamlit library**

It's now time to install the `streamlit` library:
```bash
pip install streamlit
```

## **การดำเนินการเรียกใช้แอพ Streamlit**
To launch the Streamlit demo app (Figure 1) type:
```bash
streamlit hello
```
