import os

template_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Save the Date, {}</title>
    <style>
        @font-face {{
            font-family: 'lovelace';
            src: url('../../fonts/lovelace.otf') format('opentype');
            /* You can include additional font formats here if needed */
            font-weight: normal;
            font-style: normal;
        }}
        @font-face {{
            font-family: 'alchemist';
            src: url('../../fonts/alchemist.otf') format('opentype');
            /* You can include additional font formats here if needed */
            font-weight: normal;
            font-style: normal;
        }}
        @font-face {{
            font-family: 'bdscript';
            src: url('../../fonts/bdscript.otf') format('opentype');
            /* You can include additional font formats here if needed */
            font-weight: normal;
            font-style: normal;
        }}
        @font-face {{
            font-family: 'theseasons';
            src: url('../../fonts/theseasons.ttf') format('truetype');
            /* You can include additional font formats here if needed */
            font-weight: normal;
            font-style: normal;
        }}
        .savethedate div {{
            display: inline-block;
            margin-bottom: 0px;
        }}
        .lovelace {{
            font-family: 'alchemist', Arial, Helvetica, sans-serif;
        }}
        .seasons-lg {{
            font-family: 'theseasons', Arial, Helvetica, sans-serif;
            font-size: 50px;
            letter-spacing: 5px;
        }}
        .seasons-sm {{
            font-family: 'theseasons', Arial, Helvetica, sans-serif;
            letter-spacing: 4px;
        }}
        .save {{
            margin: 0px 19px;
        }}
        .bdscript {{
            font-family: 'bdscript', Arial, Helvetica, sans-serif;
        }}
        .rotate {{
            transform: rotate(-5.33303deg);
            font-size: 83px;
            margin: 0px 15px 0px 0px;
        }}
        body {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }}
        header {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 7%;
        }}
        main {{
            text-align: center;
        }}
        img {{
            width: 100%;
            max-width: 600px;
        }}
        .centered-text {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 24px;
            font-weight: bold;
        }}
        .guest-name {{
            font-size: 60px;
            margin-left: 5px;
        }}
        .us {{
            font-size: 35px;
            margin-top: 10px;
        }}
        .card {{
            height: calc(100vh - 30px);
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add a box shadow for the raised effect */
        }}
        /* Media query for smaller screens */
        @media (max-width: 428px) {{
            .seasons-lg {{
                font-family: 'theseasons', Arial, Helvetica, sans-serif;
                font-size: 2.125rem;
                letter-spacing: 0.313rem;
            }}
            .save {{
                margin: 0 1.188rem;
                margin-left: 0rem;
            }}
            .guest-name {{
                font-size: 3.55rem;
                margin-left: 0.213rem;
            }}
            .us {{
                font-size: 1.488rem;
                margin-top: 0.425rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="card">
        <header>
            <h1 class="savethedate"><div class="seasons-lg save">SAVE</div><div class="bdscript rotate">the</div><div class="seasons-lg">DATE</div></h1>
        </header>
        <main>
            <img src="./custom-image.jpg" alt="Custom Image" onerror="this.src='../../img/eng_pics/DSC05342-sm.jpg'">
            <h3 class="lovelace">FOR THE WEDDING OF</h3>
            <h2 class="seasons-sm us">GAIL + LARRY</h2>
            <h3 class="lovelace">SEPTEMBER 14, 2024</h3>
            <h3 class="lovelace">TAIPEI, TAIWAN</h3>
            <h3 class="lovelace">FORMAL INVITATION TO FOLLOW FOR<br><span class="bdscript guest-name">{}</span>.</h3>
        </main>
    </div>
</body>
</html>
"""

# Read names from the text file (assuming names are in UTF-8 encoding)
with open('guest-list.txt', 'r', encoding='utf-8') as file:
    names = file.read().splitlines()

relative_path = "../save-the-date/"
script_directory = os.path.dirname(os.path.abspath(__file__))
absolute_path = os.path.join(script_directory, relative_path)
# Create subfolders and index.html files if they don't exist
for name in names:
    # Replace commas, ampersands, and spaces with underscores in folder names
    folder_name = name.lower().replace(", & ", "-").replace(", ", "-").replace(" & ", "-").replace(" ", "-")
    folder_path = os.path.join(absolute_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        with open(f'{folder_path}/index.html', 'w', encoding='utf-8') as html_file:
            html_file.write(template_html.format(name, name))
        print(f'Subfolder and index.html file generated for: {name}')
    else:
        print(f'Subfolder already exists for: {name}. Skipping...')
