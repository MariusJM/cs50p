import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    if url:
        output = "https://youtu.be/" + url.group(1)
#        print(output)
        return output
    else:
        return None


if __name__ == "__main__":
    main()
