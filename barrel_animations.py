from barrel_sprite import * #Importerer alt fra barrel_Sprite

#Denne koden trengs ikke lenger, men ble brukt under testing.
#Samme beskrivelse finnes under barrel.py

class barrel_sprite(BarrelAnimationSetup):
    def __init__(self, game, path='Animation/Barrel/img0.png',
                 animation_time=130):
        super().__init__(game, path, animation_time)
        self.moving_left_images = self.get_images(self.path + '/Left')
        self.moving_right_images = self.get_images(self.path + '/Right')
        self.falling_images = self.get_images(self.path + '/Falling')

    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.moving()
        self.falling()

    def moving(self):
        if self.barrel.moving_right and not self.barrel.falling:
            self.animate(self.moving_right_images)
        if not self.barrel.moving_right and not self.barrel.falling:
            self.animate(self.moving_left_images)

    def falling(self):
        if self.barrel.falling:
            self.animate(self.falling_images)