############################################################
# copy links and saved in file which name is links.txt
# if you saved another name file you should change links.txt file name in line 13
# the py and links' files must be same directory
# I do not check working another lang books, only eng books
############################################################
import os
import subprocess
import urllib.parse
import urllib.request

path = "pwd"
alink = "https://link.springer.com/"
links = "links.txt"


def direc():
    global path
    out = subprocess.run([path], stdout=subprocess.PIPE)
    path = (out.stdout.decode("utf-8"))[:-1] + "/"
    print(path)


def website():
    direc()  # current directory
    try:
        # open file that contains download links
        with open(os.path.join(path, links), "r") as files:
            count = 0
            for line in files.readlines():
                if not line.strip():
                    # file ends with a newline
                    exit(0)
                site = urllib.request.urlopen(line)
                web = site.read().decode("utf-8")
                start = web.find("<h1>")
                end = web.find("</h1>")
                title = web[start + 4 : end]

                # some title contains '/', so this is a problem such as 'does not exist
                # directory'
                while title.find("/") > 0:
                    title = title.replace("/", "-")
                title = title.replace(" ", "_") + ".PDF"
                start = web.find("content/pdf")
                end = web.find('"', start)
                linkd = alink + web[start:end]

                # download and create file on local
                urllib.request.urlretrieve(linkd, path + title)

                print(str(count) + ":" + title)
                count += 1
    except IOError:
        raise SystemExit("cannot find links.txt")


if __name__ == "__main__":
    website()
