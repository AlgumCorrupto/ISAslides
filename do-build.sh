#!/bin/bash

manim -ql scene.py Scn
manim-slides convert Scn docs/index.html
