import gradio as gr

def generate_site(title, tagline, sections, color):

    section_list = sections.split(",")

    cards = ""
    for sec in section_list:
        cards += f"""
        <div class="card">
        <h2>{sec.strip()}</h2>
        <p>This section describes {sec.strip()} information.</p>
        </div>
        """

    html = f"""
<!DOCTYPE html>
<html>
<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

*{{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Segoe UI;
}}

body{{
background:linear-gradient(135deg,{color},#141e30,#243b55);
color:white;
transition:0.5s;
}}

nav{{
display:flex;
justify-content:space-between;
padding:20px 40px;
background:rgba(0,0,0,0.4);
backdrop-filter:blur(10px);
}}

nav h1{{
font-size:24px;
}}

.hero{{
text-align:center;
padding:120px 20px;
}}

.hero h2{{
font-size:50px;
margin-bottom:20px;
}}

.hero p{{
font-size:20px;
opacity:0.8;
}}

.container{{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:25px;
padding:60px;
}}

.card{{
background:rgba(255,255,255,0.1);
padding:30px;
border-radius:15px;
backdrop-filter:blur(10px);
transition:0.4s;
box-shadow:0 10px 30px rgba(0,0,0,0.5);
}}

.card:hover{{
transform:translateY(-15px) scale(1.04);
}}

footer{{
text-align:center;
padding:30px;
opacity:0.7;
}}

button{{
padding:12px 25px;
border:none;
border-radius:25px;
background:white;
color:black;
font-weight:bold;
cursor:pointer;
}}

.toggle{{
position:fixed;
top:20px;
right:20px;
}}

</style>

<script>

function toggleTheme(){{

let body=document.body

if(body.style.background=="white"){{
body.style.background="black"
body.style.color="white"
}}

else{{
body.style.background="white"
body.style.color="black"
}}

}}

function downloadHTML(){{
var element = document.createElement('a');
var file = new Blob([document.documentElement.outerHTML], {{type:'text/html'}});
element.href = URL.createObjectURL(file);
element.download = "generated_website.html";
document.body.appendChild(element);
element.click();
}}

</script>

</head>

<body>

<div class="toggle">
<button onclick="toggleTheme()">Toggle Theme</button>
</div>

<nav>
<h1>{title}</h1>
<div>Home | About | Contact</div>
</nav>

<section class="hero">
<h2>{title}</h2>
<p>{tagline}</p>
<button onclick="downloadHTML()">Download Website</button>
</section>

<section class="container">

{cards}

</section>

<footer>
Created using HTML Quick Styler
</footer>

</body>

</html>
"""

    return html


demo = gr.Interface(
    fn=generate_site,
    inputs=[
        gr.Textbox(label="Website Title"),
        gr.Textbox(label="Tagline"),
        gr.Textbox(label="Sections (comma separated)"),
        gr.ColorPicker(label="Theme Color")
    ],
    outputs=gr.HTML(),
    title="AI HTML Quick Styler",
    description="Generate beautiful responsive websites instantly"
)

demo.launch()