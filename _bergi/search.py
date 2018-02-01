from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch_dsl.query import MultiMatch

from django.conf import settings

connections.create_connection(hosts=settings.ES_HOSTS)

# please just don't do that in future articles
MINUS_WORDS = ["öncelikle", "herkese", "merhaba", "selam", "sevgili",
				"değerli", "e-bergi", "ebergi", "bergi", "okurları",
				"okuyucuları","bu", "geçen", "ay", "ayki", "yazımda",
				"yazımızda", "sayımızda","anlatacağım", "anlatmıştık",
				"bahsetmek", "istiyorum", "çalışacağım"]

# an elasticsearch fn to "disable" ten years old articles from appearing everywhere.
# see https://www.voxxed.com/2014/12/advanced-scoring-elasticsearch/
AGEISM = {
	"gauss": {
		"date": {
			"offset": "1095d",
			"scale": "2555d",
			"decay": 0.4
		}
	}
}

class ArticleIndex(DocType):
	authors = Text()
	cats = Text(analyzer="turkish")

	title = Text(analyzer="turkish")
	content = Text(analyzer="turkish")
	date = Date()

	class Meta:
		index = 'article-index'

from . import models
def index_all():
	for a in models.Article.nondraft.all(): a.to_search().save()

def search(q):
	s = Search().query("multi_match",
				query=q,
				minimum_should_match="75%",
				fields=["authors", "cats", "title", "content"])
	hits = s.execute()
	return [models.Article.nondraft.get(pk=hit.meta.id) for hit in hits]

def recommends(a):
	s = Search().query("more_like_this",
				stop_words=MINUS_WORDS,
				like={"_id": a.pk,
					"_index": "article-index",
					"_type": "article_index"},
				fields=["authors^2", "cats", "title^2", "content"])

	search_body = {
		"query": {
			"function_score": {
				"query": s.to_dict()["query"],
				"functions": [AGEISM]
			}
		}
	}
	r = connections.get_connection().search(index="article-index", body=search_body)
	hits = r["hits"]["hits"][:settings.SUGGESTION_COUNT]
	return [models.Article.nondraft.get(pk=hit["_id"]) for hit in hits]
