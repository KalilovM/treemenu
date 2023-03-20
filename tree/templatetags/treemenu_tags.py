from django import template
from django.urls import reverse
from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_path = request.path_info.lstrip("/")
    menu_items = MenuItem.objects.filter(parent=None)
    menu_html = "<ul>"
    for item in menu_items:
        menu_html += f"<li>{render_menu_item(item,current_path)}</li>"

    menu_html += "</ul>"
    return menu_html


def render_menu_item(item, current_path):
    active = is_active(item, current_path)
    html = f'<a href="{get_menu_item_url(item)}"{" class=active" if active else ""}>{item.name}</a>'

    if active or item.children.exists():
        html = "<ul>"

        for child in item.children.all():
            html += f"<li>{render_menu_item(child,current_path)}</li>"
        html += "</ul>"
    return html


# guide how to continue


def is_active(item, current_path):
    if item.url and item.url == current_path:
        return True
    if item.named_url and item.named_url == current_path:
        return True
    return False


def get_menu_item_url(item):
    if item.url:
        return item.url
    if item.named_url:
        return reverse(item.named_url)
    return "#"


# from django.shortcuts import render
# from .models import MenuItem

# def home(request):
#     menu_items = MenuItem.objects.filter(parent=None)
#     return render(request, "home.html", {"menu_items": menu_items})
