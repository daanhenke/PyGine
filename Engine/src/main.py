import logging
import logging.handlers
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
        self.screen = pygame.display.set_mode((160, 144))

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

if __name__ == '__main__':
    pygine = Engine()
    pygine.run()
