# _bergi"s custom tags

import misaka

import datetime

from django import template
from django.utils.dateformat import format

from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name

from django.core.files.storage import default_storage
from sorl.thumbnail import get_thumbnail

register = template.Library()
html_formatter = HtmlFormatter()

class CustomRenderer(misaka.HtmlRenderer):
	# The Thumbnail creator for post contents
	def image(self, raw_url, title, alt):
		img_url = raw_url

		if not raw_url.startswith('http'):
			# The media saved in default_storage, for further info see https://www.caktusgroup.com/blog/2017/08/28/advanced-django-file-handling/
			file = default_storage.open(raw_url.split("/")[-1])

			if file is not None:
				img = get_thumbnail(file, "800x450", crop="noop", quality=80)

				if img is not None:
					img_url = img.url

		return "\n<img src=\"{}\">\n".format(img_url)

	# The code highlighter, taken from https://misaka.readthedocs.io/en/latest/#usage
	def blockcode(self, text, lang):
		try:
			lexer = get_lexer_by_name(lang)
		except ClassNotFound:
			lexer = None

		if lexer:
			return highlight(text, lexer, html_formatter)

		return "\n<pre><code>{}</code></pre>\n".format(misaka.escape_html(text.strip()))


renderer = CustomRenderer(misaka.HTML_ESCAPE)

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
