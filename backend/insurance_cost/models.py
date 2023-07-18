from django.db import models


class Rate(models.Model):
    name = models.CharField(
        verbose_name='Тариф',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Коэффициент',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name


class CargoType(models.Model):
    name = models.CharField(
        verbose_name='Груз',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Вид',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

    def __str__(self):
        return self.name


class InsuranceCost(models.Model):
    cargo_type = models.ForeignKey(
        CargoType,
        on_delete=models.CASCADE,
        related_name='costs',
        verbose_name='Груз',
    )
    rate = models.ForeignKey(
        Rate,
        on_delete=models.CASCADE,
        related_name='costs',
        verbose_name='Коэффициент',
    )
    cost = models.PositiveSmallIntegerField(
        related_name='costs',
        verbose_name='Цена',
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата запроса'
    )

    class Meta:
        verbose_name = 'Страховка'
        verbose_name_plural = 'Страховки'
        constraints = [
            models.UniqueConstraint(fields=['cargo_type', 'rate'],
                                    name='unique insurance cost')
        ]
