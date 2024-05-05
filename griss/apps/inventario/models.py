from django.db import models

class Categoria(models.Model):
    nombre=models.CharField(default='', max_length=150)
    def __str__(self):
        return str(self.nombre)
    
class Producto(models.Model):
    nombre = models.CharField(default='', max_length=200)
    descripcion = models.TimeField()
    costo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    unidades = models.IntegerField(default=1)
    def ___str__(self):
        return str(f'{self.nombre}-{self.categoria}')
