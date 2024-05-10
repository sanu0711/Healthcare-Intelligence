from django import template
from django.utils.safestring import mark_safe
import markdown as md

register = template.Library()

@register.filter
def markdown_to_html(markdown_text):
    """Converts Markdown text to HTML."""
    html_content = md.markdown(markdown_text)
    return mark_safe(html_content)
