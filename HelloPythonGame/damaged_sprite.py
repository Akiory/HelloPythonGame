import pygame
from pygame.sprite import Sprite

class Damaged_sprite(Sprite):
    """Класс спрайта повреждения"""
    def __init__(self, sprite_initiator):
        """Конструктор спрайта, принимает значение спрайта инициатора"""
        super().__init__()

        self.sprite_initiator = sprite_initiator


               
        # Загрузка анимации повреждений 
        self.raw_images = (
            pygame.image.load('images/animations/damaged/fire_1.png'),
            pygame.image.load('images/animations/damaged/fire_2.png'),
            pygame.image.load('images/animations/damaged/fire_3.png'),
            pygame.image.load('images/animations/damaged/fire_4.png'),
            pygame.image.load('images/animations/damaged/fire_5.png'),
            pygame.image.load('images/animations/damaged/fire_6.png')
        )

        self.anim_images = []
        
        # Изменяем размер картинок для анимации
        for anim_image in self.raw_images:
            anim_image = pygame.transform.scale(anim_image, (80, 80))
            self.anim_images.append(anim_image)

        # Индекс для списка
        self.anim_frame_counter = 0

        # Отображаемое Image
        self.image = self.anim_images[0]
        # Отображаемый Rect
        self.rect = self.image.get_rect()

    
            
    def update(self):
        """Перемещает пришельца вправо"""
        # self.rect.x = self.sprite_initiator.rect.x
        # self.rect.y = self.sprite_initiator.rect.y
        self.rect.center = self.sprite_initiator.rect.center
        self.update_anim()

        
            
    def update_anim(self):
        """Обновляет картинку в анимации"""
        self.anim_frame_counter += 1

        self.image = self.anim_images[self.anim_frame_counter % len(self.anim_images)]
