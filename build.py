from re import I
from pybtex.database.input import bibtex
import json

google_analytics_tracking_id = "G-93TTLCHNLY"

def get_personal_data():
    name = ["Alexandros", "Delitzas"]
    other_name = ["Alex", "Delitzas"]

    email = "alexandros.delitzas@inf.ethz.ch"
    twitter = "AlexDelitzas"
    github = "AlexDelitzas"
    # bio_text = f"""
    #             <p>I am an incoming PhD student at <a href="https://ethz.ch/en.html" target="_blank">ETH Zurich</a> and <a href="https://www.mpi-inf.mpg.de/" target="_blank">Max Planck Institute for Informatics</a>, advised by <a href="https://people.inf.ethz.ch/marc.pollefeys" target="_blank">Prof. Marc Pollefeys</a> (ETH) and <a href="https://people.mpi-inf.mpg.de/~theobalt" target="_blank">Prof. Christian Theobalt</a> (MPI), and supported by the <a href="https://learning-systems.org/" target="_blank">Max Planck ETH Center for Learning Systems</a> (CLS). I am interested in 3D Computer Vision, particularly in the areas of 3D scene understanding and generative modelling.</p>
    #             <p>Currently, I am a Computer Science MSc student at <a href="https://ethz.ch/en.html" target="_blank">ETH Zurich</a> specializing in Machine Learning. I am conducting my master thesis on 3D scene understanding supervised by <a href="https://francisengelmann.github.io" target="_blank">Francis Engelmann</a> and <a href="https://people.inf.ethz.ch/marc.pollefeys" target="_blank">Prof. Marc Pollefeys</a>. Furthermore, I conducted a research project in collaboration with the <a href="https://da.inf.ethz.ch" target="_blank">Data Analytics Lab</a>, where I worked on the intersection of 2D/3D vision and natural language. In my semester thesis, I worked on diffusion models and 3D pose transfer supervised by <a href="https://ha0tang.github.io" target="_blank">Hao Tang</a>, <a href="https://www.informatik.uni-wuerzburg.de/computervision/home/" target="_blank">Prof. Radu Timofte</a> and <a href="https://scholar.google.com/citations?user=TwMib_QAAAAJ&hl=en" target="_blank">Prof. Luc Van Gool</a>.</p> 

    #             <p>Prior to that, I was an undergraduate student in Electrical and Computer Engineering at the <a href="https://www.auth.gr/en" target="_blank">Aristotle University of Thessaloniki</a>, where I worked with <a href="https://issel.ee.auth.gr/en/staff/andreas-l-symeonidis" target="_blank">Prof. Andreas Symeonidis</a> and <a href="http://users.auth.gr/ppetrant" target="_blank">Prof. Panagiotis Petrantonakis</a>.
                
    #             <p>For any inquiries, feel free to reach out!</p>
    #             <p>
    #                 <a href="assets/pdf/CV_Delitzas.pdf" target="_blank" style="margin-right: 15px"><i class="fa fa-address-card fa-lg"></i> CV</a>
    #                 <a href="mailto:alex.delitzas@gmail.com" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
    #                 <a href="https://twitter.com/AlexDelitzas" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
    #                 <a href="https://scholar.google.com/citations?user=1NH2hXoAAAAJ&hl=en" target="_blank" style="margin-right: 15px"><i class="fa-solid fa-book"></i> Scholar</a>
    #                 <a href="https://github.com/AlexDelitzas" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
    #             </p>
    # """
    bio_text = f"""
                <p>I am a first-year PhD student at <a href="https://ethz.ch/en.html" target="_blank">ETH Zurich</a> and <a href="https://www.mpi-inf.mpg.de/" target="_blank">Max Planck Institute for Informatics</a>, advised by <a href="https://people.inf.ethz.ch/marc.pollefeys" target="_blank">Prof. Marc Pollefeys</a> (ETH) and <a href="https://people.mpi-inf.mpg.de/~theobalt" target="_blank">Prof. Christian Theobalt</a> (MPI), and supported by the <a href="https://learning-systems.org/" target="_blank">Max Planck ETH Center for Learning Systems</a> (CLS). I am interested in 3D Computer Vision, particularly in the areas of 3D/4D scene understanding and reconstruction.</p>
                <p>Previously, I obtained my MSc in Computer Science at <a href="https://ethz.ch/en.html" target="_blank">ETH Zurich</a>, specializing in machine learning and computer vision. During my studies, I conducted research projects with the <a href="https://cvg.ethz.ch" target="_blank">Computer Vision and Geometry Group</a> led by <a href="https://people.inf.ethz.ch/marc.pollefeys" target="_blank">Prof. Marc Pollefeys</a>, the <a href="https://da.inf.ethz.ch" target="_blank">Data Analytics Lab</a> led by <a href="https://scholar.google.com/citations?user=T3hAyLkAAAAJ&hl=en" target="_blank">Prof. Thomas Hofmann</a> and the <a href="https://vision.ee.ethz.ch" target="_blank">Computer Vision Lab</a> led by <a href="https://scholar.google.com/citations?user=TwMib_QAAAAJ&hl=en" target="_blank">Prof. Luc Van Gool</a>.</p> 

                <p>Prior to that, I was an undergraduate student in Electrical and Computer Engineering at the <a href="https://www.auth.gr/en" target="_blank">Aristotle University of Thessaloniki</a>, where I worked with <a href="https://people.auth.gr/symeonid/?lang=en" target="_blank">Prof. Andreas Symeonidis</a> and <a href="https://ece.auth.gr/en/staff/panagiotis-petrantonakis/" target="_blank">Prof. Panagiotis Petrantonakis</a>.</p>
                
                <p>For any inquiries, feel free to reach out!</p>
                <p>
                    <a href="mailto:alexandros.delitzas@inf.ethz.ch" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/AlexDelitzas" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=1NH2hXoAAAAJ&hl=en" target="_blank" style="margin-right: 15px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/AlexDelitzas" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h5>Homepage Template</h5>
                <p>
                    This webpage is based on the template provided by <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Michael Niemeyer</a>. I customized it to support a news section, equal contribution indications in the publications section and google analytics. Feel free to use this <a href="https://github.com/AlexDelitzas/alexdelitzas.github.io" target="_blank">version</a> or the <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">original</a> one!
                </p>
            </div>
    """
    return name, other_name, bio_text, footer

def get_author_dict():
    return {
        'Sotirios Anagnostidis': 'https://da.inf.ethz.ch/people/SotirisAnagnostidis',
        'Gregor Bachmann': 'https://da.inf.ethz.ch/people/GregorBachmann',
        'Thomas Hofmann': 'https://da.inf.ethz.ch',
        'Panagiotis Petrantonakis': 'http://users.auth.gr/ppetrant/',
        'Andreas Symeonidis': 'https://issel.ee.auth.gr/en/staff/andreas-l-symeonidis/',
        'Kyriakos Chatzidimitriou': 'https://kyrcha.info',
        'Ayca Takmaz': 'https://aycatakmaz.github.io/',
        'Robert Sumner': 'https://studios.disneyresearch.com/people/bob-sumner/',
        'Federico Tombari': 'https://federicotombari.github.io/',
        'Marc Pollefeys': 'https://people.inf.ethz.ch/marc.pollefeys/',
        'Francis Engelmann': 'https://francisengelmann.github.io/', 
        'Chenyangguang Zhang': 'https://zhangcyg.github.io', 
        'Fangjinhua Wang': 'https://fangjinhuawang.github.io',
        'Johanna Wald': 'https://scholar.google.de/citations?user=dfjN3YAAAAAJ&hl=en',
        'Maria Parelli': 'https://mparelli.github.io'
    }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Alexandros Delitzas', add_links=True, equal_contribution=None):
    links = get_author_dict() if add_links else {}
    s = ""

    equal_contributors = -1
    if equal_contribution is not None:
        equal_contributors = equal_contribution
    for idx, p in enumerate(persons):
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if idx < equal_contributors:
            string_part_i += "*"
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""

    if 'equal_contribution' in entry.fields.keys():
        s += f"""{generate_person_html(entry.persons['author'], equal_contribution=int(entry.fields['equal_contribution']))} <br>"""
    else: 
        s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""{entry.fields['title']} <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_news_html():
    s = ""
    with open('news.json') as news_data_file:
        news_data = news_data_file.read()
    parsed_news_data = json.loads(news_data)
    # print(parsed_news_data)
    for i, cur_news_data in enumerate(parsed_news_data):
        date = cur_news_data['date']
        news_description = cur_news_data['news_description_html']
        s += f"""<li style="margin-bottom: .3em;"><span style="font-weight: bold;">{date}</span>: {news_description}</li>"""

        if i < len(parsed_news_data) - 1:
            s += "\n\t\t\t\t\t"

    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    news = get_news_html()
    pub = get_publications_html()
    talks = get_talks_html()
    name, other_name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={google_analytics_tracking_id}"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', '{google_analytics_tracking_id}');
    </script>

  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]} - {other_name[0] + ' ' + other_name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="margin-bottom: 1em;">
            <h3 class="display-5" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]} (<span style="font-weight: bold;">{other_name[0]}</span> {other_name[1]})</h3>
            </div>
            <br>
            <div class="col-md-8" style="">
                {bio_text}
            </div>
            <div class="col-md-4" style="">
                <img src="assets/img/profile.jpg" class="img-thumbnail" width="280px" alt="Profile picture">
            </div>
        </div>
        <div class="row" style="margin-top: 2em;">
            <div class="col-sm-12" style="">
                <h4>News</h4>
                <ul>
                    {news}
                </ul>
            </div>
        </div>
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4>Publications</h4>
                <h6>* indicates equal contribution</h6>
                <br />
                {pub}
            </div>
        </div>
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4>Invited talks</h4>
                {talks}
            </div>
        </div>
        <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
            {footer}
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')
