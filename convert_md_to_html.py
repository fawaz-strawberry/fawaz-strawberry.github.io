import markdown
import os

# Directories
MD_DIR = 'markdown'
HTML_DIR = 'html'
ASSETS_DIR = 'assets'
GALLERY_DIR = 'gallery'

# Read the original index.html and projects.html content
with open('index_template.html', 'r') as f:
    INDEX_HTML_TEMPLATE = f.read()

with open('projects_template.html', 'r') as f:
    PROJECTS_HTML_TEMPLATE = f.read()

with open('gallery_template.html', 'r') as f:
    GALLERY_HTML_TEMPLATE = f.read()

def convert_md_to_html(md_content, title, stylesheet='../assets/style.css'):
    # Remove the title from the Markdown content
    md_content_lines = md_content.split('\n')
    if md_content_lines[0].startswith('# '):
        md_content_lines = md_content_lines[1:]
    cleaned_md_content = '\n\n'.join(md_content_lines)
    
    html_content = markdown.markdown(cleaned_md_content)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{stylesheet}">
    <title>{title}</title>
    <!-- Add the fade out and fade in script here imported from assets/startup_script.js-->
    <script src="../assets/startup_script.js"></script>
</head>
<body>
<div class="small-title">
    <a href="../index.html">Fawaz's Portfolio</a>
</div>
    <header>
        <h1>{title}</h1>
    </header>
    <main class="content">
        {html_content}
    </main>
    <footer>
        <ul class="footer-menu">
            <li><a href="https://www.instagram.com/fawaz.strawberry/">Instagram</a></li>
            <li><a href="https://github.com/fawaz-strawberry">Github</a></li>
            <li><a href="https://www.linkedin.com/in/fawaz-mujtaba/">Linkedin</a></li>
            <li><a href="../mujtaba_resume.pdf">Resume</a></li>
        </ul>
    </footer>
</body>
</html>'''

def update_main_pages(featured_projects, all_projects):
    # Update index.html
    updated_index = INDEX_HTML_TEMPLATE
    featured_projects_section = '<div class="featured-projects">\n' + featured_projects + '\n</div>'
    updated_index = updated_index.replace('<div class="featured-projects"></div>', featured_projects_section)

    with open('index.html', 'w') as f:
        f.write(updated_index)
    
    # Update projects.html
    updated_projects = PROJECTS_HTML_TEMPLATE
    projects_section = '<div class="all-projects">\n' + all_projects + '\n</div>'
    updated_projects = updated_projects.replace('<div class="all-projects"></div>', projects_section)

    with open('projects.html', 'w') as f:
        f.write(updated_projects)

def main():
    featured_projects = ''
    all_projects = ''
    md_files = [f for f in os.listdir(MD_DIR) if f.endswith('.md')]
    gallery_images = [f for f in os.listdir(GALLERY_DIR) if (f.endswith('.png') or f.endswith('.jpg'))]

    for md_file in md_files:
        with open(os.path.join(MD_DIR, md_file), 'r') as f:
            md_content = f.read()
        
        title = md_content.split('\n')[0].replace('# ', '')
        html_content = convert_md_to_html(md_content, title)
        html_file = os.path.join(HTML_DIR, md_file.replace('.md', '.html'))

        with open(html_file, 'w') as f:
            f.write(html_content)

        # Assuming the first image is used as the project thumbnail
        first_image = md_content.split('\n')[1].split('(')[1].split(')')[0]
        project_entry = f'<a href="{html_file}"><li><img src="{first_image.replace("../", "./")}" alt="{title}"></li><h2>{title}</h2></a>'
        
        if len(featured_projects.split('<a ')) <= 3:
            featured_projects += project_entry
        all_projects += project_entry

    #Add all gallery images to gallery.html


    print(all_projects)
    update_main_pages(featured_projects, all_projects)

if __name__ == '__main__':
    main()
