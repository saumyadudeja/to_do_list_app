from django.db import models

# Create your models here.
class Todo(models.Model):
    TODO="todo"
    DOING="doing"
    DONE="done"

    COMPLETION_CHOICES=(
        (TODO,"todo"),
        (DOING,"doing"),
        (DONE,"done")
    )

    task = models.CharField(max_length=60)
    completion_status = models.CharField(max_length=5,choices=COMPLETION_CHOICES,default=TODO)
    #completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.task