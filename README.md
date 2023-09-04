# Personal Website

This repository contains the python script to generate [my homepage](https://alexdelitzas.github.io/). 

This webpage is based on the template provided by [Michael Niemeyer](https://github.com/m-niemeyer/m-niemeyer.github.io). I customized it to support equal contribution indications in the publications section and google analytics. Feel free to use this version or the original one!

## How to use
1. Update and adjust the name and bio text in the function `get_personal_data` in the `build.py` file.
2. Upload your own profile photo to `assets/img/profile.jpg`.
3. Replace `publications_list.pub` with your publications. Note that the entries are crawled from top to bottom, i.e. the first entries are shown at the top. Further, the entries contain additional fields like `html`, `code`, and more, that are used to generate the links to the project page, code, etc. Check out the function `get_paper_entry` in `build.py` for more information.
4. Replace `talk_list.pub` with your talks similar to before. Check out the function `get_talk_entry` in `build.py` for more information on accepted talk fields.
5. Update the author websites in the function `get_author_dict` in `builds.py` to automatically generate the links to your co-authors' websites.
6. Run `python build.py` which automatically generates the `index.html` file - the only file you need!
7. Add credits and a link to my website; if you want me to also link to yours, send me a short message.

