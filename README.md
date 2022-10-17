# PDF to PNG Converter
This is a simple (and honestly pretty ugly) GUI around a simple PDF to PNG converter using the `pdf2image` Python library
(therefore ultimately using [Poppler](https://poppler.freedesktop.org/)). It supports basic scaling of the resulting 
images and can also remove the background of the image (which it currently does by default since this is the most common
use case for myself).

## Requirements:
- python (Tested with 3.9 and 3.10)
- argparse
- pdf2image
- Pillow
- tk

Additionally `pdf2image` requires Poppler. On Linux and Mac you can simply install this using a common package manager (brew for Mac for example). For more information please see the [`pdf2image` package description](https://pypi.org/project/pdf2image/)

## Special Considerations running on Windows:
If you want to run the software on Windows you will have to get your hands on a working version of the Poppler library
and include it in the `PATH` in order for `pdf2image` to find it. Please follow the following instructions if 
you have trouble setting it up!

### Installing Python
Easiest way is to use the Microsoft store and simply download Python there. Newest is most likely the best, so I 
recommend  the latest version. As of writing this I used version `3.10.8`, but there should be no reason why other
version should not work. Nothing fancy here.

### Installing Poppler
I recommend to use the [prebuilt Poppler releases](https://github.com/oschwartz10612/poppler-windows/releases/tag/v22.04.0-0) provided by Owen Schwartz.
![](https://hackmd.syndace.dev/uploads/upload_d33ab5a80104fc37a8c47d37f0d9ce71.png)

Unzip the archive to some easy to find location of your choice. Now you need to add `bin/` folder in the Poppler release to your `PATH` variable (see [here](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) for instructions).


## Usage
### GUI Version
In order to run the software with GUI you have to run the script `pdf_to_png.py`.
From a terminal you can do so by:
```bash
python3 pdf_to_png.py
```
![](https://hackmd.syndace.dev/uploads/upload_0ebeea8d2732f2d8552e7583926e89ff.jpg)
![](https://hackmd.syndace.dev/uploads/upload_e92ab232143d63cd23fe318d8ed0b85a.jpg)

### CLI Version
For the CLI version you need to run the script `pdf_to_png_cli.py``
```bash
(base) ➜  pdf_to_png python3 pdf_to_png_cli.py -h
usage: pdf_to_png_cli.py [-h] [-p PREFIX] [-s SCALE] [-x WIDTH] [-y HEIGHT] [-b] input

positional arguments:
  input                 Input PDF which is separated into PNGs.

options:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        A prefix to add to the file names.
  -s SCALE, --scale SCALE
                        Scale image size by scalar.
  -x WIDTH, --width WIDTH
                        Set width of resulting image
  -y HEIGHT, --height HEIGHT
                        Set height of resulting image
  -b, --with-background
                        Include PDF background

```

## FAQ
### What is the weird default width/height settings
This software was developed as a helper for the Conan Exiles mod [RavencrestCouriers](https://github.com/Thraxerrrr/RavencrestCouriers). The mod provides the possibility of rendering images inside of ingame books, therefore this software is used to convert PDFs to renderable PNGs. The pixel sizes are the closest approximation I could find for the size of the ingame books. 
My workflow consists of formatting a document using LaTeX and then converting the resulting PDF with the script (although I do most often use a version without the GUI).
