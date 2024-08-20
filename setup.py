from setuptools import setup, find_packages

print(find_packages())

setup(
    name="maskrcnn",
    version='3.0.36',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "tensorflow==2.12",
        "scikit-image==0.20.0",
        "opencv-python-headless",
        "imgaug",
        "Pillow==9.0.1",
        "imutils"
    ],
    author="https://github.com/Rene-Michel99"
)
