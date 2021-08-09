from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
	
	use_in_migrations = True

	def _create_user(self, username, password, **extra_fields):
		if not username:
			raise ValueError('Username not set')

		user = self.model(username=username, **extra_fields)
		user.set_password(password)
		user.save(using=self.db)

	def create_user(self, username, password=True, **extra_fields):
		self._create_user(username, password, **extra_fields)

	def create_superuser(self, username, password=True, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		self._create_user(username, password, **extra_fields)
