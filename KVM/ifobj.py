"""These functions can be called to manage and generate various objects that are associated with 
network interfaces. """


"""
   Copyright (c) 2014, Are Hansen

   All rights reserved.
 
   Redistribution and use in source and binary forms, with or without modification, are
   permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list
   of conditions and the following disclaimer.
 
   2. Redistributions in binary form must reproduce the above copyright notice, this
   list of conditions and the following disclaimer in the documentation and/or other
   materials provided with the distribution.
 
   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND AN
   EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
   OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
   SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
   INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
   TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
   BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
   STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
   THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import random


def genmac():
    """Generates a MAC address. The first part of the MAC address is set and belongs to a legit 
    vendor, the last part is randomly generated. """
    # Astarte Technology Co: 00:0e:8b
    mac01 = [ 0x00, 0x0e, 0x8b,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # Xensource, Inc: 00:16:3e
    mac02 = [ 0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # ProCurve Networking by HP: 00:1f:fe
    mac03 = [ 0x00, 0x1f, 0xfe,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # CISCO SYSTEMS, INC: a4:bc:c3
    mac04 = [ 0xa4, 0xbc, 0xc3,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]
    
    # Netgear: 00:26:f2
    mac05 = [ 0x00, 0x26, 0xf2,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # Cisco-Linksys, LLC: 00:25:9c
    mac06 = [ 0x00, 0x25, 0x9c,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # ASUSTek COMPUTER INC: bc:ae:c5
    mac07 = [ 0xbc, 0xae, 0xc5,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # Oracle Corporation (was: Sun Microsystems Inc.): 08:00:20
    mac08 = [ 0x08, 0x00, 0x20,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # Schenck Pegasus Corp: 00:05:fc
    mac09 = [ 0x00, 0x05, 0xfc,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # Cisco-Linksys, LLC (was: Sipura Technology, Inc): 00:0e:08
    mac10 = [ 0x00, 0x0e, 0x08,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # NETGEAR INC: 28:c6:8e
    mac11 = [ 0x28, 0xc6, 0x8e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # Sun Microsystems: 00:03:ba
    mac12 = [ 0x00, 0x25, 0x9c,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # ASUSTek COMPUTER INC: f4:6d:d4
    mac13 = [ 0xf4, 0x6d, 0xd4,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # Cisco-Linksys, LLC: c0:c1:c0
    mac14 = [ 0xc9, 0xc1, 0xc0,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # Samsung Electronics Co.,Ltd: c8:7e:75
    mac15 = [ 0xc8, 0x7e, 0x75,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]

    # CSUN System Technology Co.,LTD: bc:39:a6
    mac16 = [ 0x00, 0x25, 0x9c,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]


    mac_list = [ mac01, mac02, mac03, mac04, mac05,
                 mac06, mac07, mac08, mac09, mac10,
                 mac11, mac12, mac13, mac14, mac15,
                 mac16 ]

    mac = random.choice(mac_list)
    
    return ':'.join(map(lambda x: "%02x" % x, mac))


for i in range(160000):
    print genmac()