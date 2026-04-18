from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.
def home(request):
    return HttpResponse('<h1>welcome to torilo shop</h1>')

def product_list(request):
    dummy_products = """
        <strong><h1>Products</h1></strong>

        <p>-- nestle water 50cl pack x 12 </p>
        <p>price -- $6500</p>
        <p>-- golden morn cereal 300g </p>
        <p>price -- $3600</p>
    """
    return HttpResponse(dummy_products)

def about(request):
    about = """
        <strong><h1>About Page</h1></strong>

        <strong>
            <p>
                This is torilo shop app users can view products and buy products.
                note app is still under development.
            </p>
        </strong>
    """
    return HttpResponse(about)


def page_not_found(request, exception=None, undefined_path=None):
    messg = (
        '<h1>Page not found!!</h1>'
        f"ths request path '{request.path}' was not found on this server \n"
        f'{exception if exception else 'no route mathes this url'}'
    )
    return HttpResponseNotFound(messg,content_type="text/plain", status=404)



