#!/usr/bin/env python3

"""
Created: By Jakub Malhotra
Created: On April 2024
This is the "Space Aliens" game on the Adafruit Pybadge
"""

import stage
import ugame


def game_scene() -> None:
    """
    This is the main function game scene
    """

    # image banks for circuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank
    #   and set the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8 )

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, items show up in order 
    game.layers = [ship] + [background]

    # render all sprites
    #   most likley you will only render the background once per game scene 
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite
        game.render_sprites([ship])
        game.tick()  #wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()
