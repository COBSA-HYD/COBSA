from django.db import models
from django.contrib.auth.models import ( 
	BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from django.contrib.auth.hashers import (
	check_password, is_password_usable, make_password,
)

class MyUserManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self, username, email=None, password=None):
		if not username:
			raise ValueError('The given username must be set')
		email = self.normalize_email(email)
		user = self.model(
			username = username,
			email=email
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):
		user = self.create_user(username, email,
			password=password,
		)
		user.is_admin = True
		# user.is_staff = True
		# user.is_superuser = True
		user.save(using=self._db)
		return user

class MyUser(AbstractBaseUser):
	"""
	Custom user class.
	"""
	username = models.CharField('Username', max_length=100, unique=True, db_index=True)
	email = models.EmailField('email address',)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	last_name = models.CharField(max_length=50, blank=True)
	first_name = models.CharField(max_length=50 , blank=True)
	joined = models.DateTimeField(auto_now_add=True , null=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = MyUserManager()

	def __unicode__(self):
		return self.username

	def get_full_name(self):
		fullname = self.first_name+" "+self.last_name
		return self.fullname

	def get_short_name(self):
		return self.first_name

	@property
	def is_superuser(self):
		return self.is_admin

	@property
	def is_staff(self):
		return self.is_admin

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin

	def is_authenticated(self):
		"""
		Always return True. This is a way to tell if the user has been
		authenticated in templates.
		"""
		return True
# Create your models here.
