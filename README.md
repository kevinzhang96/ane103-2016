# Harvard ANE103 2016
This is Harvard's ANE103 website, based off the Creative template at [Bootstrapious](https://bootstrapious.com/free-templates).  We made significant changes, most notably writing scripts to generate all static content from a folder of images and captions.  This makes updating the site very easy.

The only files that need to be modified (apart from static content) are `generate.py` and the template components.  Modify the template components however you see fit; `generate.py` should only be modified to introduce new parts of the site or change how the site is structured.

The image content should be structured in subfolders in the `img` directory as follows:
- Place all images to be shown on one page in a subdirectory named appropriately
- All images should be in `jpg` format and compressed as much as possible
- Place a `captions.txt` file in the subdirectory with the name of an image (without the `.jpg` extension), followed by a tab, followed by that image's caption

Once the above is done, you can simply run `generate.py` to generate all content!
