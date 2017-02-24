import os
import sys
import xml.etree.ElementTree

colorSpaces = ["calibratedRGB"]

def help():
    print("\n")
    print("Usage: {module} <colorspace> (valid Xcode colorspace like \"calibratedRGB\") <filename>".format(module=__file__))
    print("\n")

def set_colorSpace(filename, colorSpace):
    tree = xml.etree.ElementTree.parse('Main.storyboard')
    root = tree.getroot()
    for color in root.findall('.//color'):
        if color.attrib.get('colorSpace') != "calibratedWhite":
            color.attrib.update({'colorSpace': colorSpace})
        color.attrib.pop('customColorSpace', None)
    os.rename("Main.storyboard", "Old.storyboard")
    tree.write("Main.storyboard")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        colorspace = sys.argv[1]
        filename = sys.argv[2]
        if os.path.exists(filename) and os.path.isfile(filename):
            if ".storyboard" not in filename:
                print("The input file should be a .storyboard file")
            else:
                if colorspace not in colorSpaces:
                    print("The colorspace is invalid")
                else:
                    set_colorSpace(filename, colorspace)
        else:
            print("The input is not a valid file or it doesn't exist")
    else:
        help()
