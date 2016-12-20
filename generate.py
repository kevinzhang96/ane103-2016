#!/usr/bin/python
from random import random
import os

# proportion of hover boxes (vs. labeled boxes)
ratio = 0

# all pages in this site (in sidebar order)
pages = ["casting", "brewing", "drama", "gilgamesh", "cooking", "tabula"]
allpages = ["index"] + pages

# page => display name (in sidebar)
page_names = {
    "casting": "Group A: Casting",
    "brewing": "Group B: Brewing",
    "drama": "Group D: Drama",
    "gilgamesh": "Evening Event: Gilgamesh",
    "cooking": "Evening Event: Cooking",
    "tabula": "Tabula Gratulatoria"
}

# authors
authors = {
    "brewing": "Vanessa Li",
    "casting": "Mustafa Bal",
    "drama": "Kristen Fang",
    "cooking": "Matthew Ryan"
}

# read in contents of component pages
lines = {}
with open("components/header.html") as h:
    lines["header"] = h.readlines()
with open("components/footer.html") as f:
    lines["footer"] = f.readlines()
with open("components/portfolio_start.html") as ps:
    lines["ps_start"] = ps.readlines()
with open("components/portfolio_end.html") as pe:
    lines["ps_end"] = pe.readlines()
with open("components/sidebar_start.html") as sds:
    lines["sd_start"] = sds.readlines()
with open("components/sidebar_mid.html") as sdm:
    lines["sd_mid"] = sdm.readlines()
with open("components/sidebar_end.html") as sde:
    lines["sd_end"] = sde.readlines()
with open("components/body_start.html") as bs:
    lines["body_start"] = bs.readlines()
with open("components/body_end.html") as be:
    lines["body_end"] = be.readlines()
with open("components/image_box_p1.html") as p1:
    lines["p1"] = p1.readlines()
with open("components/image_box_p2a.html") as p2a:
    lines["p2a"] = p2a.readlines()
with open("components/image_box_p2b.html") as p2b:
    lines["p2b"] = p2b.readlines()
with open("components/image_box_p3.html") as p3:
    lines["p3"] = p3.readlines()

# sidebar generator
def sidebar(curr_page, link=None):
    sd_lines = []
    sd_lines += lines["sd_start"]
    for page in allpages:
        title = "Home" if page == "index" else page_names[page]
        parts = [
            "                ",
            "<li class=\"active\"><a href=\"" if page == curr_page else "<li><a href=\"",
            page,
            ".html\">",
            title,
            "</a></li>\n"
        ]
        sd_lines.append("".join(parts))
    sd_lines += lines["sd_mid"]
    if link != None:
        sd_lines.append(link)
    sd_lines += lines["sd_end"]
    return sd_lines

# image box generator
def image_box(uri, caption):
    sd_lines = []
    sd_lines += lines["p1"]
    if random() < ratio:
        parts = [
            "                  ",
            "<div class=\"box-masonry\"><a href=\"\" title=\"\" class=\"box-masonry-image with-hover-overlay\"><img src=\"",
            uri,
            "\" alt=\"\" class=\"img-responsive\"></a>\n"
        ]
        sd_lines.append("".join(parts))
        sd_lines += lines["p2a"]
    else:
        parts = [
            "                  ",
            "<div class=\"box-masonry\"><img src=\"",
            uri,
            "\" alt=\"\" class=\"img-responsive\">\n"
        ]
        sd_lines.append("".join(parts))
        sd_lines += lines["p2b"]
    sd_lines.append("                        <p>" + caption.strip() + "</p>\n")
    sd_lines += lines["p3"]
    return sd_lines

# create index page first
print "writing index.html"
with open("index.html", "wb") as f:
    f.writelines(lines["header"])
    f.writelines(sidebar("index"))
    with open("components/index_body.html") as ib:
        f.writelines(ib.readlines())
    f.writelines(lines["footer"])

for page in pages:
    has_images = os.path.exists("img/" + page)
    has_summary = os.path.exists("components/" + page + "_summary.html")
    print "writing " + page + ".html"
    with open(page + ".html", "wb") as f:
        f.writelines(lines["header"])
        link = ""
        if page in authors:
            link = "<p class=\"sidebar-p\">\n"
            link += "Photos by %s. " % authors[page]
            link += "Read their journal <a href=\"files/%s.pdf\" target=\"_blank\">here.</a>\n" % page
            link += "</p>\n"
            if page == "brewing":
                link += "<p class=\"sidebar-p\">See their photo series "
                link += "<a href=\"https://www.dropbox.com/sh/1m2is9zj9cvcaxv/AACPHh5y4Db3W9-5Y22iS2Jja?dl=0\">here.</a>"
                link += "</p>\n"
        f.writelines(sidebar(page, link))
        f.writelines(lines["body_start"])
        if has_summary:
            with open("components/" + page + "_summary.html") as s:
                f.writelines(s.readlines())
        if has_images:
            f.writelines(lines["ps_start"])
            captions = {}
            with open("img/" + page + "/captions.txt") as c:            
                for line in c:
                    tokens = line.split("\t")
                    captions[tokens[0] + ".jpg"] = tokens[1]
            for filename in os.listdir("img/" + page):
                if filename.endswith(".jpg"): 
                    f.writelines(image_box("img/" + page + "/" + filename, captions[filename]))
            f.writelines(lines["ps_end"])
        f.writelines(lines["body_end"])
        f.writelines(lines["footer"])

print "generate.py done"
