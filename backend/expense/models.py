from django.db import models

from backend.core.models import TimeStampedModel


class Expense(TimeStampedModel):
    description = models.CharField('descrição', max_length=50)
    payment_date = models.DateField('data de pagamento', null=True, blank=True)
    value = models.DecimalField('valor', max_digits=7, decimal_places=2)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        ordering = ('id',)
        verbose_name = 'despesa'
        verbose_name_plural = 'despesas'

    def __str__(self):
        return self.description
