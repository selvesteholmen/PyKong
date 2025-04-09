from player_sprite import *

#Ny klasse for animasjonene
class sprite(animationsetup):
    def __init__(self, game, path='Animation/Player/img0.png', #Path er stien til filene
                 animation_time=70):
        super().__init__(game, path, animation_time) #Lager en ny innit som jeg kan styre utenom vanlige init
        self.idle_left_images = self.get_images(self.path + '/IdleL') #Lager "Ferdig animationer" ved å finne bildene som tilhører riktig animasjon, med andre ord. "Denne animasjonen = Disse bildene"
        self.idle_right_images = self.get_images(self.path + '/IdleR')
        self.left_images = self.get_images(self.path + '/WalkL')
        self.right_images = self.get_images(self.path + '/WalkR')
        self.jump_left_images = self.get_images(self.path + '/JumpL')
        self.jump_right_images = self.get_images(self.path + '/JumpR')
        self.idle_climb_images = self.get_images(self.path + '/IdleC')
        self.climb_images = self.get_images(self.path + '/Climbing')

    #Oppdaterer alle funskjonene
    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.idle()
        self.moving_right()
        self.moving_left()
        self.jump()
        self.climbing()

    #Hver av disse funskjonene er hver sinn animasjon, de velger hvilkene bilde frekvenser som skal bli satt i self.animate utifra kriterie
    def idle(self):
        if self.player.idle and not self.player.is_jumping and not self.player.climbing:
            if self.player.last_movement_right:
                self.animate(self.idle_right_images)
            else:
                self.animate(self.idle_left_images)
        if self.player.climbing and self.player.idle:
            self.animate(self.idle_climb_images)

    def jump(self):
        if self.player.is_jumping and not self.player.climbing:
            if self.player.last_movement_right:
                self.animate(self.jump_right_images)
            else:
                self.animate(self.jump_left_images)

    def moving_right(self):
        if self.player.moving_right and self.player.idle == False and self.player.is_jumping == False:
            self.animate(self.right_images)

    def moving_left(self):
        if self.player.moving_left and self.player.idle == False and self.player.is_jumping == False:
            self.animate(self.left_images)

    def climbing(self):
        keys = pg.key.get_pressed()
        if self.player.climbing:
            if keys[pg.K_s] or keys[pg.K_w]:
                self.animate(self.climb_images)
