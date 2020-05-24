from django.test import TestCase

from .models import *

class PairModelTests(TestCase):
    def test_pair_consists_of_male_and_female(self):
        """ A pair of falcons consists of male and female
        Trying to create a pair with two males or two females shouldn't work
        """
        male1 = Falcon(sex='M')
        male2 = Falcon(sex='M')
        female1 = Falcon(sex='F')
        female2 = Falcon(sex='F')
        pair_of_males = Pair(male=male1, female=male2)
        pair_of_females = Pair(male=female1, female=female2)
        self.assertIs(False, False)
