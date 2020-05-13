from django.db import models

# Models for breeding app

class Falcon(models.Model):
    """ Model for a single falcon """

    SEX = [
        ('M', 'male'),
        ('F', 'female')
    ]
    
    name = models.CharField(max_length=30, null=True, blank=True)
    ring = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    species_latin = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX)
    birth_date = models.DateField()
    CITES_num = models.CharField(max_length=30)
    CITES_img = models.ImageField()
    registration_img = models.ImageField()
    RDOS_permission_img = models.ImageField()
    in_aviary = models.ForeignKey('Aviary', on_delete=models.CASCADE)
    in_pair = models.ForeignKey('Pair', on_delete=models.CASCADE)
    father = models.ForeignKey('self', on_delete=models.CASCADE, related_name='_father')
    mother = models.ForeignKey('self', on_delete=models.CASCADE, related_name='_mother')
    siblings = models.ManyToManyField('self', related_name='_sibling')
    width_young = models.PositiveSmallIntegerField()
    length_young = models.PositiveSmallIntegerField()
    weight_young = models.PositiveSmallIntegerField()
    photos_young = models.ImageField()
    width_old = models.PositiveSmallIntegerField()
    length_old = models.PositiveSmallIntegerField()
    weight_old = models.PositiveSmallIntegerField()
    photos_old = models.ImageField()

    def __str__(self):
        return 'Falcon name: ' + str(self.name) + ', ring: ' + str(self.ring)

class Pair(models.Model):
    """ Model for a breeding pair """
    
    male = models.ForeignKey(Falcon, on_delete=models.CASCADE, related_name='+')
    female = models.ForeignKey(Falcon, on_delete=models.CASCADE, related_name='+')
    offspring = models.ManyToManyField(Falcon)

    def __str__(self):
        print(self.keys())
        return 'Pair:\nmale name: ' + str(self.male.name) + ', ring: ' + str(self.male.ring) + ';\n' + 'female name: ' + str(self.female.name) + ', ring: ' + str(self.female.ring)

class Aviary(models.Model):
    """ Model for a single aviary """
    
    occupied = models.BooleanField()
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    falcons = models.ManyToManyField(Falcon)

    def __str__(self):
        return 'Aviary id: ' + str(self.id) + '\noccupied: ' + str(self.occupied)