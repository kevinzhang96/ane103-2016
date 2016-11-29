#!/usr/bin/python
from random import random
import os

# proportion of hover boxes (vs. labeled boxes)
ratio = 0.5

# all pages in this site
pages = ["brewing", "casting", "drama"]
allpages = ["index"] + pages

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
with open("components/sidebar_end.html") as sde:
    lines["sd_end"] = sde.readlines()
with open("components/image_box_p1.html") as p1:
    lines["p1"] = p1.readlines()
with open("components/image_box_p2a.html") as p2a:
    lines["p2a"] = p2a.readlines()
with open("components/image_box_p2b.html") as p2b:
    lines["p2b"] = p2b.readlines()
with open("components/image_box_p3.html") as p3:
    lines["p3"] = p3.readlines()

# sidebar generator
def sidebar(curr_page):
    sd_lines = []
    sd_lines += lines["sd_start"]
    for page in allpages:
        title = "Home" if page == "index" else page.capitalize()
        parts = [
            "                ",
            "<li class=\"active\"><a href=\"" if page == curr_page else "<li><a href=\"",
            page,
            ".html\">",
            title,
            "</a></li>\n"
        ]
        sd_lines.append("".join(parts))
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
with open("index.html", "ab+") as f:
    f.writelines(lines["header"])
    f.writelines(sidebar("index"))
    with open("components/index_body.html") as ib:
        f.writelines(ib.readlines())
    f.writelines(lines["footer"])

for page in pages:
    with open(page + ".html", "ab+") as f:
        f.writelines(lines["header"])
        f.writelines(sidebar(page))
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
        f.writelines(lines["footer"])