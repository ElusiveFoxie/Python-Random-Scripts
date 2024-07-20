import shutil
from pathlib import Path

# Variables
src_files = "fonts_source"
output_path = "fonts_output"

# Paths
fonts_dir = Path(src_files) / "fonts"
index_html = Path(src_files) / "index.html"
src_style_css = Path(src_files) / "style.css"

# Create output directory if it doesn't exist
Path(output_path).mkdir(parents=True, exist_ok=True)

# Function to handle each font file
def handle_font_file(font_file):
    font_name = font_file.stem
    font_ext = font_file.suffix.lower()
    
    site_dir = Path(output_path) / f"site_{font_name}"
    site_fonts_dir = site_dir / "fonts"
    
    # Create directories
    site_dir.mkdir(parents=True, exist_ok=True)
    site_fonts_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy index.html to the new site directory
    shutil.copy(index_html, site_dir / "index.html")
    
    # Create style.css file in the new site directory
    site_style_css = site_dir / "style.css"
    with open(site_style_css, 'w') as css_file:
        if font_ext == ".ttf":
            css_file.write(f"""
@font-face {{
    font-family: 'CustomFont';
    src: url('fonts/{font_file.name}') format('truetype');
}}
""")
        elif font_ext == ".otf":
            css_file.write(f"""
@font-face {{
    font-family: 'CustomFont';
    src: url('fonts/{font_file.name}') format('opentype');
}}
""")
        # Append contents of the source style.css
        with open(src_style_css, 'r') as src_css_file:
            css_file.write(src_css_file.read())
    
    # Copy font file to the new fonts directory
    shutil.copy(font_file, site_fonts_dir / font_file.name)

# Count files in the fonts directory
font_files = list(fonts_dir.glob("*.*"))
print(f"Found {len(font_files)} font files.")

# Process each font file
for font_file in font_files:
    handle_font_file(font_file)
