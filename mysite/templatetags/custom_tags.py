from django import template
from django.urls import reverse

register = template.Library()


def link_to_section(url_name, section_id):
    return reverse(url_name) + '#' + section_id


@register.simple_tag
def link_to_formation_section(url_name, formation_pk):
    return link_to_section(url_name, f'formation-{formation_pk}')
