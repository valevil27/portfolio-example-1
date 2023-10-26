from django.shortcuts import render, HttpResponse

html_base = """
<h1> Mi web personal </h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca De</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>
"""


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse(
        html_base
        + """
                        <h2>Acerca de</h2>
                        <p>Me llamo Eduardo y soy programador</p>
                        """
    )


def portfolio(request):
    return HttpResponse(
        html_base
        + """
                        <h2>Portfolio</h2>
                        <p>This is my portfolio with several beautiful projects.</p>                        
                        """
    )


def contact(request):
    return HttpResponse(
        html_base
        + """
                        <h2>Portfolio</h2>
                        <p>Contact me:</p>                        
                        <ul>
                            <li>Email: evalerovilella@gmail.com</li>
                            <li>Instagram: @valevil96</li>
                            <li>GitHub: <a href="https://www.github.com/Swamptk">Swamptk</a></li>
                        """
    )
