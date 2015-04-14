#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unit tests for jointmoments.

"""
from __future__ import division
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(HERE, os.pardir))
sys.path.insert(0, os.path.join(HERE, os.pardir, "jointmoments"))

from jointmoments import *

tolerance = 1e-5

def test_jointmoments():
    unbias = 0
    data = [[ 0.837698,  0.49452,  2.54352 ],
            [-0.294096, -0.39636,  0.728619],
            [-1.62089 , -0.44919,  1.20592 ],
            [-1.06458 , -0.68214, -1.12841 ],
            [ 2.14341 ,  0.7309 ,  0.644968],
            [-0.284139, -1.133  ,  1.98615 ],
            [ 1.19879 ,  2.55633, -0.526461],
            [-0.032277,  0.11701, -0.249265],
            [-1.02516 , -0.44665,  2.50556 ],
            [-0.515272, -0.578  ,  0.515139],
            [ 0.259474, -1.24193,  0.105051],
            [ 0.178546, -0.80547, -0.016838],
            [-0.607696, -0.21319, -1.40657 ],
            [ 0.372248,  0.93341, -0.667086],
            [-0.099814,  0.52698, -0.253867],
            [ 0.743166, -0.79375,  2.11131 ],
            [ 0.109262, -1.28021, -0.415184],
            [ 0.499346, -0.95897, -2.24336 ],
            [-0.191825, -0.59756, -0.63292 ],
            [-1.98255 , -1.5936 , -0.935766],
            [-0.317612,  1.33143, -0.46866 ],
            [ 0.666652, -0.81507,  0.370959],
            [-0.761136,  0.10966, -0.997161],
            [-1.09972 ,  0.28247, -0.846566]]
    rows = len(data)
    cols = len(data[0])
    
    coskew_result = coskew(data, rows, cols, unbias)
    cokurt_result = cokurt(data, rows, cols, unbias)

    # expected_coskew = np.array([[
    #     [ 0.153993 ,  0.161605 ,   0.131816 ],
    #     [ 0.161605 ,  0.433037 ,  -0.035224 ],
    #     [ 0.131816 , -0.035224 ,   0.0136523],
    # ], [
    #     [ 0.161605 ,  0.433037 ,  -0.035224 ],
    #     [ 0.433037 ,  0.899048 ,  -0.314352 ],
    #     [-0.035224 , -0.314352 ,  -0.29955  ],
    # ], [
    #     [ 0.131816 ,  -0.035224,   0.0136523],
    #     [-0.035224 ,  -0.314352,  -0.29955  ],
    #     [ 0.0136523,  -0.29955 ,   1.06208  ],
    # ]])
    expected_coskew = np.array([[
        [ 0.147577 ,   0.154872 ,  0.126324  ],
        [ 0.154872 ,   0.414994 , -0.0337563 ],
        [ 0.126324 ,  -0.0337563,  0.0130835 ],
    ], [
        [ 0.154872 ,   0.414994 , -0.0337563 ],
        [ 0.414994 ,   0.861588 , -0.301254  ],
        [-0.0337563,  -0.301254 , -0.287068  ],
    ], [
        [ 0.126324 ,  -0.0337563,   0.0130835],
        [-0.0337563,  -0.301254 ,  -0.287068 ],
        [ 0.0130835,  -0.287068 ,   1.01782  ],
    ]])
    expected_cokurt = np.array([
        [[
            [ 2.12678  ,  1.11885   ,  0.474782  ],
            [ 1.11885  ,  1.12294   ,  0.187331  ],
            [ 0.474782 ,  0.187331  ,  1.15524   ],
        ], [
            [ 1.11885  ,   1.12294  ,   0.187331 ],
            [ 1.12294  ,   1.40462  ,  -0.0266349],
            [ 0.187331 ,  -0.0266349,   0.276558 ],
        ], [
            [ 0.474782 ,   0.187331 ,  1.15524   ],
            [ 0.187331 ,  -0.0266349,  0.276558  ],
            [ 1.15524  ,   0.276558 ,  0.178083  ],
        ]], [[
            [ 1.11885  ,   1.12294  ,   0.187331 ],
            [ 1.12294  ,   1.40462  ,  -0.0266349],
            [ 0.187331 ,  -0.0266349,   0.276558 ],
        ], [
            [ 1.12294  ,   1.40462  , -0.0266349 ],
            [ 1.40462  ,   3.10288  , -0.517198  ],
            [-0.0266349,  -0.517198 ,  0.779221  ],
        ], [
            [ 0.187331 ,  -0.0266349,  0.276558  ],
            [-0.0266349,  -0.517198 ,  0.779221  ],
            [ 0.276558 ,   0.779221 ,  0.218732  ],
        ]], [[
            [ 0.474782 ,  0.187331  ,  1.15524   ],
            [ 0.187331 , -0.0266349 ,  0.276558  ],
            [ 1.15524  ,  0.276558  ,  0.178083  ],
        ], [
            [ 0.187331 ,  -0.0266349,  0.276558  ],
            [-0.0266349,  -0.517198 ,  0.779221  ],
            [ 0.276558 ,   0.779221 ,  0.218732  ],
        ], [
            [ 1.15524  ,  0.276558  ,  0.178083  ],
            [ 0.276558 ,  0.779221  ,  0.218732  ],
            [ 0.178083 ,  0.218732  ,  5.98947   ],
        ]]
    ])

    assert((np.array(coskew_result) - expected_coskew < tolerance).all())
    assert((np.array(cokurt_result) - expected_cokurt < tolerance).all())

if __name__ == "__main__":
    reports = [[1, 1, 0, 0],
               [1, 0, 0, 0],
               [1, 1, 0, 0],
               [1, 1, 1, 0],
               [0, 0, 1, 1],
               [0, 0, 1, 1]]
    num_voters = len(reports)
    num_events = len(reports[0])
    test_jointmoments()
