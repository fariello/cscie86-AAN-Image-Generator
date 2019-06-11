#!/usr/bin/env python3

import argparse
import os
import sys
import svgwrite
from svgwrite import cm, mm, px
import numpy as np



class NodeDecoration(object):
    def __init__(self, drw, height = 4.0, width = 8.0):
        if arrowhead_nook_depth is None:
            arrowhead_nook_depth = arrowhead_thickness
            pass
        self.x_0 = 0
        self.x_1 = arrowhead_thickness
        self.x_2 = arrowhead_nook_depth
        self.x_3 = width / 2.0
        self.x_4 = width - arrowhead_nook_depth
        self.x_5 = width - arrowhead_thickness
        self.x_6 = width
        self.y_0 = 0
        self.y_2 = height / 2.0
        self.y_1 = self.y_2 - (arrowbody_height / 2.0)
        self.y_3 = self.y_2 + (arrowbody_height / 2.0)
        self.y_4 = height
        self.width = width
        self.height = height
        self.style = "fill:none;stroke:black;stroke-width:0.5;alpha=0.5"
        self.scale = 1.0
        pass


    def set_arrowhead_parameters(self, breadth = 0.5, length = 0.25, nook_offset = None):
                   """
           |------------width---------------|
                              length  c-----d
                               offset b-----d
    +-c           i                   c       --y_0   c-+
    |            /|                   |\               |
    |           / |                   | \              |
    h          /  |                   |  \             |
    e    +- a-/---j-------------------b---\-k --y_1    |
    i    |  |/             |               \|          |
    g    |  h--------------o----------------d --y_2   d-+
    h    |  |\             |               /|          |
    t    +- g-----m-------------------f---/-l --y_3   arrowhead_height
    |    |     \  |                   |  /
    |    |      \ | \      |        / | /   |
    |    |       \|  \     |       /  |/    |
    +-g  |        n   \    |      /   e     | --y_4
         |             |   |     |          |
         |  |     |    |   |     |    |     |
         | x_0   x_1  x_2 x_3   x_4  x_5   x_6
         |
         arrowbody_height
        """


    def get_double_arrow(self, drw, scale = 1.0):
        d=['M', self.x_0 * self.scale, self.y_2 * self.scale, # h
           'L', self.x_1 * self.scale, self.y_4 * self.scale, # n
           'L', self.x_2 * self.scale, self.y_3 * self.scale, # m
           'L', self.x_4 * self.scale, self.y_3 * self.scale, # f
           'L', self.x_5 * self.scale, self.y_4 * self.scale, # e
           'L', self.x_6 * self.scale, self.y_2 * self.scale, # d
           'L', self.x_5 * self.scale, self.y_0 * self.scale, # c
           'L', self.x_4 * self.scale, self.y_1 * self.scale, # b
           'L', self.x_2 * self.scale, self.y_1 * self.scale, # j
           'L', self.x_1 * self.scale, self.y_0 * self.scale, # i
           'Z']
        print(d)
        return drw.path(d=d,id="double-arrow",style=self.style)

    def get_right_arrow(self, drw, scale = 1.0):
        d=['M', self.x_0 * self.scale, self.y_2 * self.scale, # g
           'L', self.x_4 * self.scale, self.y_3 * self.scale, # f
           'L', self.x_5 * self.scale, self.y_4 * self.scale, # e
           'L', self.x_6 * self.scale, self.y_2 * self.scale, # d
           'L', self.x_5 * self.scale, self.y_0 * self.scale, # c
           'L', self.x_4 * self.scale, self.y_1 * self.scale, # b
           'L', self.x_0 * self.scale, self.y_1 * self.scale, # a
           'Z']
        print(d)
        return drw.path(d=d,id="right-arrow",style=self.style)

    def get_left_arrow(self, drw, scale = 1.0):
        d=['M', self.x_0 * self.scale, self.y_2 * self.scale, # h
           'L', self.x_1 * self.scale, self.y_4 * self.scale, # n
           'L', self.x_2 * self.scale, self.y_3 * self.scale, # m
           'L', self.x_6 * self.scale, self.y_3 * self.scale, # l
           'L', self.x_6 * self.scale, self.y_1 * self.scale, # k
           'L', self.x_2 * self.scale, self.y_1 * self.scale, # j
           'L', self.x_1 * self.scale, self.y_0 * self.scale, # i
           'Z']
        print(d)
        return drw.path(d=d,id="double-arrow",style=self.style)

    def get_grid(self,drw, scale = 1.0):
        g = drw.g()
        # Horizontals
        g.add(drw.line(
            start=(self.x_0 * self.scale, self.y_0 * self.scale),
            end=(self.x_6 * self.scale, self.y_0 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_0 * self.scale, self.y_1 * self.scale),
            end=(self.x_6 * self.scale, self.y_1 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_0 * self.scale, self.y_2 * self.scale),
            end=(self.x_6 * self.scale, self.y_2 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_0 * self.scale, self.y_3 * self.scale),
            end=(self.x_6 * self.scale, self.y_3 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_0 * self.scale, self.y_4 * self.scale),
            end=(self.x_6 * self.scale, self.y_4 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        # Verticals
        g.add(drw.line(
            start=(self.x_0 * self.scale, self.y_0 * self.scale),
            end=(self.x_0 * self.scale, self.y_4 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_1 * self.scale, self.y_0 * self.scale),
            end=(self.x_1 * self.scale, self.y_4 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_2 * self.scale, self.y_0 * self.scale),
            end=(self.x_2 * self.scale, self.y_4 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_3 * self.scale, self.y_0 * self.scale),
            end=(self.x_3 * self.scale, self.y_4 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_4 * self.scale, self.y_0 * self.scale),
            end=(self.x_4 * self.scale, self.y_4 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_5 * self.scale, self.y_0 * self.scale),
            end=(self.x_5 * self.scale, self.y_4 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        g.add(drw.line(
            start=(self.x_6 * self.scale, self.y_0 * self.scale),
            end=(self.x_6 * self.scale, self.y_4 * self.scale),
            style="stroke:#FF0000;stroke-width:0.1;alpha=0.5")
        )
        return g
    pass

arr = ArrowDecoration(height = 4, width = 8, arrowbody_height = 1.5, arrowhead_thickness = 2.25, arrowhead_nook_depth = 2)
arr.scale = 1.0

canvas = svgwrite.Drawing(
    filename="rarr.svg",
    debug=True,
    size=('%dmm' % (arr.width * arr.scale),'%dmm' % (arr.height * arr.scale)),
    viewBox=('0 0 %d %d' %(arr.height* arr.scale, arr.width * arr.scale))
)

canvas.add(arr.get_double_arrow(canvas))
#canvas.add(arr.get_grid(canvas))
canvas.save()
p
