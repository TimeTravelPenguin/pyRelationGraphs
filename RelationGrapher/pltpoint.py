"""
Author: Phillip Smith c3322845
Contact: c3322845@uon.edu.au
Will I do your homework? No.
"""

from numbers import Number

from matplotlib import pyplot as plt


class Point:
    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y

    def connectToPoint(self, p: 'Point', arrow_length=True, arrow_head_width=0.04, arrow_head_length=0.07) -> None:
        dx = p.x - self.x
        dy = p.y - self.y
        plt.arrow(self.x, self.y, dx, dy, length_includes_head=arrow_length, head_width=arrow_head_width,
                  head_length=arrow_head_length)
