import argparse
from util import read_pdf

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input", help="Input PDF which is separated into PNGs.")
    parser.add_argument(
        "-p", "--prefix", help="A prefix to add to the file names.", default=""
    )
    parser.add_argument("-s", "--scale", help="Scale image size by scalar.", default=1)

    parser.add_argument("-x", "--width", help="Set width of resulting image", default=854)
    parser.add_argument("-y", "--height", help="Set height of resulting image", default=854)
    parser.add_argument("-b", "--with-background", help="Include PDF background", action="store_true", default=False)

    args = parser.parse_args()
    scale = args.scale
    width = int(args.width)
    height = int(args.height)
    page_size = (width * scale, height * scale)
    images = read_pdf(args.input, page_size=page_size, transparent=args.with_background)

    prefix = args.prefix + "_" if args.prefix != "" else ""
    for i, image in enumerate(images):
        path = "{}page_{}.png".format(prefix, i)
        image.save(path)
        print("Saving image to: {}".format(path))
