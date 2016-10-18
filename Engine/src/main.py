import logging
import logging.handlers
import os

import colourlib
import pygame

#REMEMBER TO ~STEAL~ PORT CODE FOR 15 BIT COLOR CONVERTION: http://www.budmelvin.com/dev/15bitconverter.html

class Engine(object):
    def __init__(self):
        #Set up the ==LOGGER==
        self.logger = logging.getLogger("Engine")
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        consoleHandler.setFormatter(formatter)
        self.logger.addHandler(consoleHandler)

        tcpHandler = logging.handlers.SocketHandler("localhost", 1337)
        tcpHandler.setLevel(logging.DEBUG)
        tcpHandler.setFormatter(formatter)
        self.logger.addHandler(tcpHandler)

        fileHandler = logging.FileHandler("pygine.log", "a")
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)

        self.logger.info("Logging has been initialized")

        #Set up ==PYGAME==
        pygame.init()
        self.screen = pygame.display.set_mode((320, 288))
        self.clock = pygame.time.Clock()

    def colortest_run(self):
        self.colour = 0x0000
        self.running = True

        self.logger.info("Starting colour test..")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.colour += 8
            self.colour &= colourlib.bit15_max_value

            currentcol = colourlib.bit15_to_tuple(self.colour)
            print self.colour, currentcol

            self.screen.fill(currentcol)
            pygame.display.update()
            self.clock.tick(60)


    def palettetest_run(self):
        self.running = True
        self.simscreen = pygame.Surface((160, 144))
        self.image = pygame.image.load(os.path.join("..", "Sprite-0001.bmp"))

        self.palette = self.image.get_palette()
        print self.palette
        self.pos = -1
        self.image.set_palette(((255, 0, 255, 255), (255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)))

        self.logger.info("Starting palette & sprite test..")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.simscreen.blit(self.image, (0, 0))
            pygame.transform.scale(self.simscreen, (320, 288), self.screen)
            pygame.display.update()
            self.clock.tick(1)



if __name__ == '__main__':
    pygine = Engine()
    pygine.palettetest_run()
