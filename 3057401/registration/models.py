from django.db import models


class Polyclinic(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Поликлиника'
        verbose_name_plural = 'Поликлиники'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Специальность')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return self.name


VISIT_TIME = [('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('14-15', '14-15'),
              ('15-16', '15-16'), ('16-17', '16-17')]


class Order(models.Model):
    polyclinic = models.CharField(max_length=50, verbose_name='Поликлиника',
                                  choices=[(polyclinic.__str__(), polyclinic.__str__()) for
                                           polyclinic in
                                           Polyclinic.objects.all()])
    doctor = models.CharField(max_length=50, verbose_name='Доктор',
                              choices=[(doctor.__str__(), doctor.__str__()) for doctor in
                                       Doctor.objects.all()])
    visit_time = models.CharField(max_length=50, verbose_name='Время визита', choices=VISIT_TIME)
    full_name = models.CharField(max_length=50, verbose_name='ФИО')
    policy_number = models.PositiveIntegerField(verbose_name='Номер полиса')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)
