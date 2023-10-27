from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description =models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    # auto_now_add is executed only on creation
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    # auto_now is executed when we update the model
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Edición")
    
    class Meta:
        verbose_name = "proyecto"
        # If not specified, just adds a 's' to the end of the single one
        verbose_name_plural = "proyectos"
        # We can specify more than 1 field for ordering. '-' means desc
        ordering = ["-created"]
    
    def __str__(self):
        return self.title