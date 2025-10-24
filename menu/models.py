from django.db import models

# Create your models here.
class Menu(models.Model):
    """ Menus model """
    
    MAIN_TITLE_LIST = (
        (0, 'MAIN MENU'),
        (1, 'KIDS'),
        (2, 'SUNDAY'),
        (3, 'BEERS & CIDERS'),
        (4, 'WINES'),
        (5, 'OTHER DRINKS')
    )
    
    SUB_MENU_LIST = (
        (0, 'STARTERS'),
        (1, 'MAINS'),
        (2, 'STEAKS'),
        (3, 'PIES'),
        (4, 'BURGERS'),
        (5, 'SIDES'),
        (6, 'DESSERTS'),
        (7, 'VEGGIES'),
        (8, 'ICE CREAM'),
        (9, 'DRINKS'),
        (10, 'PICK & MIX'),
        (11, 'ROASTS'),
        (12, 'KIDS ROASTS'),
        (13, 'BEER'),
        (14, 'CIDER'),
        (15, 'WINES'),
        (16, 'WHITE'),
        (17, 'RED'),
        (18, 'SPARKLING'),
        (19, 'SOFT DRINKS')
    )
    
    main_title = models.IntegerField(choices=MAIN_TITLE_LIST)
    sub_menu_title = models.IntegerField(choices=SUB_MENU_LIST)
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.item_name