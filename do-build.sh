#!/bin/bash

manim -qh scene.py Scn
manim-slides convert Scn docs/index.html
