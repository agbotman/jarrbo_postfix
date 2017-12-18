from django.db import models

class VirtualDomain(models.Model):
	"""
	The virtual_mailbox_domains in Postfix
	Emails for this domain are handled by Postfix
	Valid users are defined in VirtualUser
	"""
	name = models.CharField(max_length=100, unique=True)
	
class VirtualUser(models.Model):
	"""
	Users for which email is handled by Postfix
	"""
	domain = models.ForeignKey('VirtualDomain')
	email = models.EmailField
	password = models.CharField(max_length=150)
	
class VirtualAlias(models.Model):
	"""
	Aliases for email addresses in virtual domains
	"""
	domain = models.ForeignKey('VirtualDomain')
	source = models.CharField(max_length=100, unique=True)
	destination = models.CharField(max_length=100, unique=True)