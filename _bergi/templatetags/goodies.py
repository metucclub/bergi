# _bergi's custom tags

import misaka
from misaka import HtmlRenderer

import datetime

from django import template
from django.utils.dateformat import format

register = template.Library()

renderer = HtmlRenderer()
md = misaka.Markdown(renderer,
	extensions=misaka.EXT_FENCED_CODE | misaka.EXT_NO_INTRA_EMPHASIS | misaka.EXT_TABLES |
			misaka.EXT_AUTOLINK | misaka.EXT_SPACE_HEADERS | misaka.EXT_STRIKETHROUGH | misaka.EXT_SUPERSCRIPT)

@register.filter
def markdown(text):
	return md(text)

# only show past years
@register.filter
def datefmt(date):
	now = datetime.datetime.now()
	if date.year == now.year:
		return format(date, "j F")
	return format(date, "j F Y")
