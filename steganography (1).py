import sys
import image_merge as image
import hide_text as text


def main():
    if len(sys.argv) > 2:
        steg(sys.argv[1], sys.argv[2])
    else:
        desteg(sys.argv[1])


def steg(cover_path, hidden_path):

    if hidden_path[-4:] == '.txt':
        text.encrypt(cover_path, hidden_path)
    else:
        image.merge(cover_path, hidden_path)


def desteg(image_path):

    try:
        text.decrypt(image_path)
    except:
        image.unmerge(image_path)


if __name__ == "__main__":
    main()
