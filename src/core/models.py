from django.db import models

class Publisher(models.Model):
	'A publisher like Ubiquity Press or University of California Press'
	name = models.CharField(max_length=300, help_text='Publisher like Ubiquity Press or University of California Press')
	doi_prefix = models.CharField(max_length=20, help_text='Publisher\'s CrossRef prefix')

	crossref_username = models.CharField(max_length=100, blank=True, null=True)
	crossref_password = models.CharField(max_length=100, blank=True, null=True)

	facebook_client_id = models.CharField(max_length=200, blank=True, null=True)
	facebook_client_secret = models.CharField(max_length=200, blank=True, null=True)

	def __unicode__(self):
		return u'%s' % self.name

	def __repr__(self):
		return u'%s' % self.name

class Publication(models.Model):
	'A book, article or other published object'
	publisher = models.ForeignKey(Publisher)
	title = models.CharField(max_length=1000)
	identifier = models.CharField(max_length=200, help_text='Should be a doi, eg. 10.5334/cg.aa')
	canonical_url = models.URLField(max_length=2000, help_text='Full URL with FQDN excluding http://')
	date_published = models.DateField()

	def __unicode__(self):
		return u'%s' % self.title

	def __repr__(self):
		return u'%s' % self.title

class Tweet(models.Model):
	'A tweet'
	publication = models.ForeignKey(Publication)
	content = models.TextField()
	user = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	profile_image = models.CharField(max_length=400)
	url = models.URLField()
	enabled = models.BooleanField(default=True)

	date = models.DateField()

	def __unicode__(self):
		return u'%s' % self.content

	def __repr__(self):
		return u'<Tweet %s>' % self.content

class Facebook(models.Model):
	'A count of Facebook mentions'
	publication = models.ForeignKey(Publication)
	share_count = models.IntegerField(default=0)
	like_count = models.IntegerField(default=0)
	comment_count = models.IntegerField(default=0)
	click_count = models.IntegerField(default=0)
	total_count = models.IntegerField(default=0)

	date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return u'%s %s' % (self.publication.name, self.total_count)

	def __repr__(self):
		return u'<Facebook %s>' % (self.publication.name, self.total_count)

class Citation(models.Model):
	'A crossref citation'
	publication = models.ForeignKey(Publication)
	doi = models.CharField(max_length=200)
	journal_title = models.CharField(max_length=2000)
	article_title = models.CharField(max_length=2000)
	year = models.IntegerField(blank=True, null=True)
	volume = models.IntegerField(blank=True, null=True)
	issue = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return u'%s %s' % (self.publication.title, self.doi)

	def __repr__(self):
		return u'<Facebook %s>' % (self.publication.title, self.doi)


## UTIL MODELS ##

def q_choices():
	return (
		('twitter', 'Twitter'),
		('crossref', 'Crossref'),
	)

class Queue(models.Model):
	publication = models.ForeignKey(Publication)
	source = models.CharField(max_length=100, choices=q_choices())


class TwitterCredential(models.Model):
	'Twitter Credentials use to pull data'
	consumer_key = models.CharField(max_length=300)
	consumer_secret = models.CharField(max_length=300)
	access_token = models.CharField(max_length=300)
	access_token_secret = models.CharField(max_length=300)
	last_used = models.DateTimeField()