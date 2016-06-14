from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class RegisteredAddress(models.Model):
    """
    The address of a registered company. Subset of data format used by
    opencorporates.com. Attribute 'region' was left out.
    """
    street_address = models.CharField(
        max_length=80,
        verbose_name=u'Street')
    postal_code = models.CharField(
        max_length=25,
        verbose_name=u'Postal Code'
    )
    locality = models.CharField(
        max_length=80,
        verbose_name=u'City'
    )
    country = models.CharField(
        max_length=80,
        verbose_name=u'Country'
    )


class Company(models.Model):
    """
    A registered company. The attributes are a subset of the data format used
    by opencorporates.com, which should be adequate to describe most companies.
    """
    company_name = models.CharField(
        max_length=80,
        verbose_name=u'Company Name'
    )
    company_number = models.CharField(
        max_length=25,
        verbose_name=u'Company Number (CVR)'
    )
    registered_address = models.ForeignKey(
        RegisteredAddress,
        verbose_name=u'Registered Address'
    )


class Customer(models.Model):
    """
    A company buying our services.
    """
    company_id = models.ForeignKey(Company, verbose_name=u'Company')


class Platform(models.Model):
    """
    A platform e.g. Django, Drupal, Alfresco... etc.
    """
    name = models.CharField(max_length=80, verbose_name=u'Designation')
    description = models.TextField(verbose_name=u'Description')


class HostingProvider(models.Model):
    """
    A hosting provider. A company providing hosting services i.e. physical or
    virtual servers.
    """
    company_id = models.ForeignKey(Company, verbose_name=u'Company')


class Server(models.Model):
    """
    A physical or virtual server.
    """
    name = models.CharField(max_length=80, verbose_name=u'Name')
    operating_system = models.CharField(
        max_length=80,
        verbose_name=u'Operating System'
    )

    responsible = models.ForeignKey(
        User,
        verbose_name=u'Ansvarlig'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=u'Description'
    )
    ssh_key_login_only = models.BooleanField(
        default=False,
        verbose_name=u'SSH key login only'
    )
    backup = models.TextField(
        null=True,
        blank=True,
        verbose_name=u'Backup'
    )
    updates = models.TextField(
        null=True,
        blank=True,
        verbose_name=u'OS/System Updated'
    )
    hostname = models.CharField(
        max_length=25,
        verbose_name=u'Hostname'
    )
    hosting_provider_id = models.ForeignKey(
        HostingProvider,
        verbose_name=u'Udbyder'
    )


class Solution(models.Model):
    """
    A software solution.
    """
    WEB_SITE = 0
    MAIL_SERVICE = 1

    TYPE_CHOICES = (
        (WEB_SITE, u'Website'),
        (MAIL_SERVICE, u'Mailserver'),
    )
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        verbose_name=u'Type'
    )
    type_other = models.CharField(
        max_length=50,
        verbose_name=u'Other',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=80, verbose_name=u'Name')
    description = models.TextField(verbose_name=u'Description')
    platform_id = models.ForeignKey(Platform, verbose_name=u'Platform')
    customer_id = models.ForeignKey(Customer, verbose_name=u'Customer')
    server_id = models.ForeignKey(Server, verbose_name=u'Server')


class Domain(models.Model):
    """
    A mapping between domain (DNS) and a server.
    """
    url = models.CharField(max_length=80, verbose_name=u'URL')
    ip_address = models.TextField(
        max_length=15,
        verbose_name=u'IP Address'
    )
    server_id = models.ForeignKey(Server, verbose_name=u'Server')
    name = models.CharField(max_length=80, verbose_name=u'Name')


class Contact(models.Model):
    """
    An external contact related to a company/organisation.
    """
    name = models.CharField(
        max_length=80,
        verbose_name=u'Name'
    )
    email = models.CharField(
        max_length=80,
        verbose_name=u'Email'
    )
    phone = models.CharField(
        max_length=80,
        verbose_name=u'Phone'
    )
    company_id = models.ForeignKey(
        Company,
        verbose_name=u'Company'
    )
