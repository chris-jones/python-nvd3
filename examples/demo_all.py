#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""
from nvd3 import lineChart
from nvd3 import lineWithFocusChart
from nvd3 import stackedAreaChart
from nvd3 import multiBarHorizontalChart
from nvd3 import linePlusBarChart
from nvd3 import cumulativeLineChart
import random
import datetime
import time


start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
nb_element = 100

#Open File for test
output_file = open('test_demo_all.html', 'w')
#---------------------------------------

type = "lineChart"
chart = lineChart(name=type, date=True, height=350)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
xdata = range(nb_element)
xdata = map(lambda x: start_time + x * 1000000000, xdata)
ydata = [i + random.randint(1, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)

kwargs1 = {'color': 'green'}
kwargs2 = {'color': 'red'}

extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
chart.add_serie(name="Count", y=ydata, x=xdata, extra=extra_serie, **kwargs1)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(name="Duration", y=ydata2, x=xdata, extra=extra_serie, **kwargs2)

chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

type = "lineWithFocusChart"
chart = lineWithFocusChart(name=type, date=True)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

xdata = range(nb_element)
xdata = map(lambda x: start_time + x * 1000000000, xdata)
ydata = [i + random.randint(-10, 10) for i in range(nb_element)]

ydata2 = map(lambda x: x * 2, ydata)
ydata3 = map(lambda x: x * 3, ydata)
ydata4 = map(lambda x: x * 4, ydata)

kwargs1 = {'color': 'green'}
kwargs2 = {'color': 'red'}
kwargs3 = {'color': 'yellow'}
kwargs4 = {'color': 'blue'}
extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
#extra_serie = None
chart.add_serie(name="serie 1", y=ydata, x=xdata, extra=extra_serie, **kwargs1)
chart.add_serie(name="serie 2", y=ydata2, x=xdata, extra=extra_serie, **kwargs2)
chart.add_serie(name="serie 3", y=ydata3, x=xdata, extra=extra_serie, **kwargs3)
chart.add_serie(name="serie 4", y=ydata4, x=xdata, extra=extra_serie, **kwargs4)

chart.buildhtml()

output_file.write(chart.htmlcontent)

#---------------------------------------

type = "stackedAreaChart"
chart = stackedAreaChart(name=type, height=350)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

xdata = range(nb_element)
xdata = map(lambda x: 100 + x, xdata)
ydata = [i + random.randint(1, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)

extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
chart.add_serie(name="serie 1", y=ydata, x=xdata, extra=extra_serie)
chart.add_serie(name="serie 2", y=ydata2, x=xdata, extra=extra_serie)

chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

type = "linePlusBarChart"
chart = linePlusBarChart(name=type, height=350, date=True)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

xdata = range(nb_element)
xdata = map(lambda x: start_time + x * 1000000000, xdata)
ydata = [i + random.randint(1, 10) for i in range(nb_element)]
ydata2 = [i + random.randint(1, 10) for i in reversed(range(nb_element))]
kwargs = {}
kwargs['bar'] = True
extra_serie = {"tooltip": {"y_start": "$ ", "y_end": ""}}
chart.add_serie(name="Count", y=ydata, x=xdata, extra=extra_serie, **kwargs)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(name="Duration", y=ydata2, x=xdata, extra=extra_serie)

chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

type = "cumulativeLineChart"
chart = cumulativeLineChart(name=type, height=350, date=True)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

xdata = range(nb_element)
xdata = map(lambda x: start_time + x * 1000000000, xdata)
ydata = [i + random.randint(1, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)

extra_serie = {"tooltip": {"y_start": "", "y_end": " Calls"}}
chart.add_serie(name="Count", y=ydata, x=xdata, extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " Min"}}
chart.add_serie(name="Duration", y=ydata2, x=xdata, extra=extra_serie)

chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

type = "multiBarHorizontalChart"
chart = multiBarHorizontalChart(name=type, height=350)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

nb_element = 10
xdata = range(nb_element)
ydata = [random.randint(-10, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)
extra_serie = {"tooltip": {"y_start": "", "y_end": " Calls"}}
chart.add_serie(name="Count", y=ydata, x=xdata, extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " Min"}}
chart.add_serie(name="Duration", y=ydata2, x=xdata, extra=extra_serie)

chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

#close Html file
output_file.close()
