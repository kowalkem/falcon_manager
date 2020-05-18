from django.db import models

# Models for breeding app

class Falcon(models.Model):
    """ Model for a single falcon """

    SEX = [
        ('M', 'male'),
        ('F', 'female')
    ]
    
    name = models.CharField(max_length=30, null=True, blank=True)
    ring = models.CharField(max_length=30, null=True, blank=True)
    species = models.CharField(max_length=30, null=True, blank=True)
    species_latin = models.CharField(max_length=30, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    CITES_num = models.CharField(max_length=30, null=True, blank=True)
    CITES_img = models.FileField(null=True, blank=True, upload_to='falcon_docs/')
    registration_img = models.FileField(null=True, blank=True, upload_to='falcon_docs/')
    RDOS_permission_img = models.FileField(null=True, blank=True, upload_to='falcon_docs/')
    in_aviary = models.ForeignKey('Aviary', on_delete=models.CASCADE, null=True, blank=True)
    in_pair = models.ForeignKey('Pair', on_delete=models.CASCADE, null=True, blank=True)
    father = models.ForeignKey('self', on_delete=models.CASCADE, related_name='_father', null=True, blank=True)
    mother = models.ForeignKey('self', on_delete=models.CASCADE, related_name='_mother', null=True, blank=True)
    siblings = models.ManyToManyField('self', related_name='_sibling', blank=True)
    width_young = models.PositiveSmallIntegerField(null=True, blank=True)
    length_young = models.PositiveSmallIntegerField(null=True, blank=True)
    weight_young = models.PositiveSmallIntegerField(null=True, blank=True)
    photos_young = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='_photos_young', null=True, blank=True)
    width_old = models.PositiveSmallIntegerField(null=True, blank=True)
    length_old = models.PositiveSmallIntegerField(null=True, blank=True)
    weight_old = models.PositiveSmallIntegerField(null=True, blank=True)
    photos_old = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='_photos_old', null=True, blank=True)

    def get_fields_for_template(self):
        return [(field.name, field.verbose_name, field.value_to_string(self)) for field in Falcon._meta.fields]

    def __str__(self):
        return 'Falcon name: ' + str(self.name) + ', ring: ' + str(self.ring)

class Pair(models.Model):
    """ Model for a breeding pair """
    
    male = models.ForeignKey(Falcon, on_delete=models.CASCADE, related_name='+')
    female = models.ForeignKey(Falcon, on_delete=models.CASCADE, related_name='+')
    offspring = models.ManyToManyField(Falcon, blank=True)

    def __str__(self):
        return 'Pair:\nmale name: ' + str(self.male.name) + ', ring: ' + str(self.male.ring) + ';\n' + 'female name: ' + str(self.female.name) + ', ring: ' + str(self.female.ring)

class Aviary(models.Model):
    """ Model for a single aviary """
    
    occupied = models.BooleanField()
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE, null=True, blank=True)
    falcons = models.ManyToManyField(Falcon, blank=True)
    last_cleaned = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'Aviary id: ' + str(self.id) + '\noccupied: ' + str(self.occupied)

class Photo(models.Model):
    """ Model to enable saving multiple photos per falcon """

    img = models.ImageField(null=True, blank=True, upload_to='falcon_imgs/')

    def __str__(self):
        return 'Falcon Photo'