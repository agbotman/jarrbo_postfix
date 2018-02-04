from django.db import models

class VirtualDomain(models.Model):
	"""
	The virtual_mailbox_domains in Postfix
	Emails for this domain are handled by Postfix
	Valid users are defined in VirtualUser
	"""
	name = models.CharField(max_length=100, unique=True)
	
	def __str__(self):
		return self.name
	
class VirtualUser(models.Model):
	"""
	Users for which email is handled by Postfix
	"""
	domain = models.ForeignKey('VirtualDomain', 
								on_delete=models.CASCADE)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=150)
	description = models.CharField(max_length=150, null=True, blank=True)
	
	def __str__(self):
		return self.email
	
class VirtualAlias(models.Model):
	"""
	Aliases for email addresses in virtual domains
	"""
	domain = models.ForeignKey('VirtualDomain',
								on_delete=models.CASCADE)
	source = models.CharField(max_length=100, unique=True)
	destination = models.CharField(max_length=100)
	description = models.CharField(max_length=150, null=True, blank=True)
	
	class Meta:
		verbose_name_plural = "Aliases"

	def __str__(self):
		return self.source