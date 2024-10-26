import os
import re
import math
import random
import markdown
import yaml
from PIL import Image

# Directories
MD_DIR = 'markdown'         # Directory containing Markdown files for projects
HTML_DIR = 'html'           # Directory to save generated HTML files
ASSETS_DIR = 'assets'       # Directory containing assets like CSS and JS
GALLERY_DIR = 'gallery'     # Directory containing gallery images

# Read the HTML templates for index, projects, and gallery pages
with open('index_template.html', 'r') as f:
    INDEX_HTML_TEMPLATE = f.read()

with open('projects_template.html', 'r') as f:
    PROJECTS_HTML_TEMPLATE = f.read()

with open('gallery_template.html', 'r') as f:
    GALLERY_HTML_TEMPLATE = f.read()

def generate_keyframes(animation_name, max_translate=15, max_rotate=2, steps=10):
    """
    Generates CSS keyframes for floating animations.

    Parameters:
    - animation_name (str): Name of the animation.
    - max_translate (float): Maximum translation in pixels.
    - max_rotate (float): Maximum rotation in degrees.
    - steps (int): Number of steps in the animation.

    Returns:
    - str: CSS keyframes for the animation.
    """
    keyframes = f"@keyframes {animation_name} {{\n"
    for step in range(steps + 1):
        percentage = (step / steps) * 100
        # Use sine and cosine functions to generate smooth movement
        translate_x = max_translate * math.sin(math.radians(percentage * 3.6))  # 0 to 360 degrees
        translate_y = max_translate * math.cos(math.radians(percentage * 3.6))
        rotate = max_rotate * math.sin(math.radians(percentage * 7.2))  # Faster rotation
        keyframes += f"    {percentage:.1f}% {{ transform: translate({translate_x:.2f}px, {translate_y:.2f}px) rotate({rotate:.2f}deg); }}\n"
    keyframes += "}\n"
    return keyframes

def generate_all_keyframes(num_animations=6):
    """
    Generates multiple keyframe animations.

    Parameters:
    - num_animations (int): Number of different animations to generate.

    Returns:
    - str: Combined CSS keyframes for all animations.
    """
    keyframes_css = ""
    for i in range(1, num_animations + 1):
        # Slightly vary the max_translate and max_rotate for each animation
        max_translate = random.uniform(10, 20)  # Increase values for more prominent effect
        max_rotate = random.uniform(1, 3)
        steps = 20  # More steps for smoother animation
        animation_name = f"float{i}"
        keyframes_css += generate_keyframes(animation_name, max_translate, max_rotate, steps)
    return keyframes_css

def write_css_file(css_content, css_file_path='assets/style.css'):
    """
    Writes the combined CSS content to a file.

    Parameters:
    - css_content (str): The CSS content to write.
    - css_file_path (str): The path to the CSS file.
    """
    with open(css_file_path, 'w') as css_file:
        css_file.write(css_content)

def convert_md_to_html(md_content, title, stylesheet='../assets/style.css'):
    """
    Converts Markdown content to an HTML page.

    Parameters:
    - md_content (str): The Markdown content to convert.
    - title (str): The title of the HTML page.
    - stylesheet (str): The path to the CSS stylesheet.

    Returns:
    - str: The full HTML page as a string.
    """
    # Remove the title from the Markdown content to avoid duplication
    md_content_lines = md_content.split('\n')
    if md_content_lines[0].startswith('# '):
        md_content_lines = md_content_lines[1:]
    cleaned_md_content = '\n\n'.join(md_content_lines)
    
    # Convert the cleaned Markdown content to HTML
    html_content = markdown.markdown(cleaned_md_content)
    
    # Construct the full HTML page
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="{stylesheet}">
    <!-- Include the startup script -->
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
            <li><a href="https://www.linkedin.com/in/fawaz-mujtaba/">LinkedIn</a></li>
            <li><a href="../mujtaba_resume.pdf">Resume</a></li>
            <li><a href="privacypolicy.html">Privacy Policy</a></li>
        </ul>
    </footer>
</body>
</html>'''

def update_main_pages(featured_projects, all_projects):
    """
    Updates the index.html and projects.html pages with the generated project cards.

    Parameters:
    - featured_projects (str): HTML content for the featured projects.
    - all_projects (str): HTML content for all projects.
    """
    # Insert the featured projects into index.html
    updated_index = INDEX_HTML_TEMPLATE.replace(
        '<div class="featured-projects"></div>',
        f'<div class="card-column">\n{featured_projects}\n</div>'
    )

    with open('index.html', 'w') as f:
        f.write(updated_index)
    
    # Insert all projects into projects.html
    updated_projects = PROJECTS_HTML_TEMPLATE.replace(
        '<div class="all-projects"></div>',
        f'<div class="card-column">\n{all_projects}\n</div>'
    )

    with open('projects.html', 'w') as f:
        f.write(updated_projects)

def generate_card(image_src, caption, link=None, is_gallery=False):
    """
    Generates HTML code for a project or gallery card.

    Parameters:
    - image_src (str): Path to the image source.
    - caption (str): Caption or title for the card.
    - link (str): URL to link the card to (for projects).
    - is_gallery (bool): Flag to indicate if the card is for the gallery.

    Returns:
    - str: HTML code for the card.
    """
    # Get image dimensions
    if os.path.exists(image_src):
        with Image.open(image_src) as img:
            width, height = img.size
    else:
        width, height = 200, 200  # Default size if image not found

    # Apply a scale factor
    scale_factor = random.uniform(0.5, 0.7)
    max_card_size = 400  # Limit maximum size
    card_width = min(int(width * scale_factor), max_card_size)
    card_height = min(int(height * scale_factor), max_card_size)

    # Generate animation properties
    animation_duration = random.uniform(50, 100)  # Longer durations
    animation_delay = random.uniform(-animation_duration, 0)  # Negative delay
    animation_names = [f'float{i}' for i in range(1, 11)]
    animation_name = random.choice(animation_names)

    # Inline styles for each card
    style = f"""
        width: {card_width}px;
        height: {card_height}px;
        animation-name: {animation_name};
        animation-duration: {animation_duration}s;
        animation-delay: {animation_delay}s;
        animation-timing-function: ease-in-out;
        animation-iteration-count: infinite;
        animation-fill-mode: forwards;
        animation-direction: alternate;
        position: relative;
        will-change: transform;
    """

    # Generate card HTML with the 'card-image' class
    if is_gallery:
        card_html = f'''
        <div class="card" onclick="openModal('{image_src}', `{caption}`)" style="{style}">
            <img class="card-image" src="{image_src}" alt="{caption}">
            <div class="caption">{caption}</div>
        </div>
        '''
    else:
        card_html = f'''
        <div class="card" style="{style}">
            <a href="{link}">
                <img class="card-image" src="{image_src}" alt="{caption}">
                <div class="caption">{caption}</div>
            </a>
        </div>
        '''
    return card_html

def main():
    """
    Main function to generate the website pages with updated content.
    """
    # Generate the dynamic keyframes CSS
    keyframes_css = generate_all_keyframes(num_animations=10)
    
    # Read the static CSS content
    with open('assets/static_style.css', 'r') as static_css_file:
        static_css = static_css_file.read()
    
    # Combine the static CSS with the dynamic keyframes
    full_css = static_css + '\n' + keyframes_css
    
    # Write the combined CSS to the style.css file
    write_css_file(full_css, css_file_path='assets/style.css')

    featured_projects = ''  # HTML content for featured projects on the index page
    all_projects = ''       # HTML content for all projects on the projects page

    # List all Markdown files in the projects directory
    md_files = [f for f in os.listdir(MD_DIR) if f.endswith('.md')]

    # List all images in the gallery directory
    gallery_images = [f for f in os.listdir(GALLERY_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Process each Markdown file to create project pages and cards
    for md_file in md_files:
        with open(os.path.join(MD_DIR, md_file), 'r') as f:
            md_content = f.read()
        
        # Extract the title from the first line of the Markdown content
        title = md_content.split('\n')[0].replace('# ', '')

        # Convert Markdown content to HTML
        html_content = convert_md_to_html(md_content, title)
        
        # Add class="content-image" to images in the HTML content
        html_content = re.sub(r'<img ', r'<img class="content-image" ', html_content)

        # Determine the output HTML file path
        html_file = os.path.join(HTML_DIR, md_file.replace('.md', '.html'))

        # Write the converted HTML content to a file
        with open(html_file, 'w') as f:
            f.write(html_content)

        # Extract the first image from the Markdown content as the thumbnail
        first_image_line = md_content.split('\n')[1]
        if '(' in first_image_line and ')' in first_image_line:
            first_image = first_image_line.split('(')[1].split(')')[0]
        else:
            first_image = 'default_thumbnail.png'  # Use a default image if none found

        # Adjust the image source path
        image_src = first_image.replace('../', './')

        # Generate the project card
        card_html = generate_card(image_src, title, link=html_file, is_gallery=False)

        # Add the card to featured projects or all projects
        if featured_projects.count('<div class="card"') < 3:
            featured_projects += card_html
        all_projects += card_html

    # Load captions for gallery images from a YAML file
    with open('captions.yaml', 'r') as f:
        captions = yaml.safe_load(f)

    gallery_cards = ''  # HTML content for gallery cards

    # Process each image in the gallery
    for image in gallery_images:
        # Get the caption for the image, if available
        caption = captions.get(image, '')
        image_src = os.path.join(GALLERY_DIR, image)

        # Generate the gallery card
        card_html = generate_card(image_src, caption, is_gallery=True)
        gallery_cards += card_html

    # Insert the gallery cards into the gallery template
    updated_gallery_html = GALLERY_HTML_TEMPLATE.replace(
        '<div class="all-photos"></div>',
        f'<div class="all-photos">{gallery_cards}</div>'
    )

    # Write the updated gallery HTML to a file
    with open('gallery.html', 'w') as f:
        f.write(updated_gallery_html)

    # Update the main pages with the generated project cards
    update_main_pages(featured_projects, all_projects)

if __name__ == '__main__':
    main()
