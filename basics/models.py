from django.db import models

class EmployeeDetails(models.Model):
    EMP_ID = models.CharField(max_length=100)
    EMP_NAME = models.CharField(max_length=255)
    EMP_COMP_ID = models.CharField(max_length=100)
    EMP_MAILID = models.EmailField(max_length=255)
    EMP_PHONENO = models.CharField(max_length=20)
    EMP_DOJ = models.DateField()
    EMP_ROLE_NAME = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.EMP_NAME


class VisitorDetails(models.Model):
    VS_ID = models.CharField(max_length=20)
    VS_NAME = models.CharField(max_length=100)
    VS_DATE = models.DateField()
    VS_PHONENO = models.CharField(max_length=15)
    VS_MAILID = models.EmailField()
    VS_PURPOSE = models.CharField(max_length=255)
    VS_REMARKS = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.VS_NAME

class VisitorRequest(models.Model):
    VS_ID = models.CharField(max_length=20)
    VS_NAME = models.CharField(max_length=100)
    VS_DATE = models.DateField()
    VS_PHONENO = models.CharField(max_length=15)
    VS_MAILID = models.EmailField()
    VS_PURPOSE = models.CharField(max_length=255)
    VS_REMARKS = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.VS_NAME

