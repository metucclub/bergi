# _bergi's custom tags

import markdown as Markdown
import datetime

from django import template
from django.utils.dateformat import format

register = template.Library()

@register.filter
def markdown(text):
	return Markdown.markdown(text, safe_mode="escape")

# only show past years
@register.filter
def datefmt(date):
	now = datetime.datetime.now()
	if date.year == now.year:
		return format(date, "j F")
	return format(date, "j F Y")
