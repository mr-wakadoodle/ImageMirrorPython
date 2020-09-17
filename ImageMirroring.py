from simpleimage import SimpleImage


def main():
    image = SimpleImage("original.jpg")
    height = image.height
    width = image.width

    # Create blank image for mirroring I
    mirror = SimpleImage.blank(width * 2, height)

    # Create blank image for mirroring II
    mirror_collage = SimpleImage.blank(width * 4, height * 2)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            # I mirroring
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel((width * 2) - (x + 1), y, pixel)

            # II mirroring
            # Horizontally
            mirror_collage.set_pixel(x, y, pixel)
            mirror_collage.set_pixel(width + x, y, pixel)
            mirror_collage.set_pixel((width * 3) - (x + 1), y, pixel)
            mirror_collage.set_pixel((width * 4) - (x + 1), y, pixel)

            # Vertically
            mirror_collage.set_pixel(x, height + y, pixel)
            mirror_collage.set_pixel(width + x, height + y, pixel)
            mirror_collage.set_pixel((width * 3) - (x + 1), height + y, pixel)
            mirror_collage.set_pixel((width * 4) - (x + 1), height + y, pixel)

    image.show()

    mirror.show()
    mirror.pil_image.save("Mirroring_I.png")

    mirror_collage.show()
    mirror_collage.pil_image.save("Mirroring_II.png")


if __name__ == '__main__':
    main()
