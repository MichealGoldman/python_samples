from PIL import ImageFile

def imageCheck(file):
    parser = ImageFile.Parser()
    fp = open(file, "rb")
    try:
        while True:
            data = fp.read(1024)
            if not data:
                break
            parser.feed(data)
        image = parser.close()
    except IOError as e:
        print 'Bad Image: %s' % e


