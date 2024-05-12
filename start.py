import PIL
from PIL import Image
import algorithm
import webbrowser

def main(filename: str, outname: str = "out.png"):
    image = Image.open(filename)
    img = algorithm.alg(image)
    img.save(outname)
    webbrowser.open(outname)

if __name__ == "__main__":
    fn = "in.png"
    main(fn)