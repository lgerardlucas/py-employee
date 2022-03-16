from django.db import models

class Register(models.Model):
	CHOICES_DEPARTMENT = (
        	('-', '-----'),
        	('T', 'Tester'),
        	('D', 'Developer'),
        	('R', 'RH'),
    	)
	name = models.CharField('Name:', max_length=50, blank=False, null=False)
	email = models.EmailField('E-mail:', max_length=250, blank=True, null=True)
	department = models.CharField('Departamento:', max_length=1, choices=CHOICES_DEPARTMENT, null=True, blank=True, default="-")

	class Meta:
		verbose_name = 'Register'
		verbose_name_plural = 'Registers'
