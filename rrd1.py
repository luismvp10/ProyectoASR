#!/usr/bin/env python

import rrdtool
ret = rrdtool.create("net3.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inoctets:COUNTER:600:U:U",
                     "DS:outoctets:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:10",
                     "RRA:AVERAGE:0.5:6:20")



ret = rrdtool.create("net4.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inIpv4:COUNTER:600:U:U",
                     "DS:outIpv4:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:10",
                     "RRA:AVERAGE:0.5:6:20")

ret = rrdtool.create("net5.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inIcmp:COUNTER:600:U:U",
                     "DS:outIcmp:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:10",
                     "RRA:AVERAGE:0.5:6:20")

ret = rrdtool.create("net6.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inIP:COUNTER:600:U:U",
                     "DS:outIP:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:10",
                     "RRA:AVERAGE:0.5:6:20")
et = rrdtool.create("net7.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inSnmp:COUNTER:600:U:U",
                     "DS:outSnmp:COUNTER:600:U:U,
                     "RRA:AVERAGE:0.5:1:10",
                     "RRA:AVERAGE:0.5:6:20")


if ret:
    print rrdtool.error()

