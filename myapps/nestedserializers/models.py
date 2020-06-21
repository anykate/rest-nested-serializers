from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Marks(models.Model):
    maths = models.PositiveIntegerField()
    physics = models.PositiveIntegerField()
    computers = models.PositiveIntegerField()
    student = models.ForeignKey(
        Student,
        related_name='marks',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'marks'
        verbose_name_plural = 'marks'

    def __str__(self):
        return self.student.name
