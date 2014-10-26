"""This module holds all the functions that are unique to kvmbuild.py. """

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


__author__ = 'Are Hansen'
__date__ = '2014, October 26'
__version__ = '0.0.5'


import argparse
import os
import sys
import VMBuilder
from KVM.generate.ifobj import macaddress
from KVM.validate.access import is_found
from KVM.validate.kvmenv import gname
from KVM.validate.networkobj import check_ipv4


def parse_args():
    """Defines the command line arguments. """
    parser = argparse.ArgumentParser('Build a KVM guest:')

    kvm = parser.add_argument_group('- KVM')
    kvm.add_argument('-N', dest='kvmname', help='KVM name', required=True)
    kvm.add_argument('-I', dest='ipv4add', help='KVM IPv4 address', required=True)

    paths = parser.add_argument_group('- Paths')
    paths.add_argument('-T', dest='confdir', help='Path to template directory', required=True)
    paths.add_argument('-D', dest='destdir', help='Full path to storage location', required=True)

    args = parser.parse_args()

    return args


def check_args(args):
    """Process the command line arguments and check that everything is in place. """
    if os.getuid() != 0:
        print '[ERROR]: You must be root to run this script!!'
        sys.exit(1)

    name = gname(args.kvmname)
    cdir = is_found(args.confdir)
    ddir = is_found(args.destdir)
    ipv4 = check_ipv4(args.ipv4add)
    vmbd = is_found('/usr/bin/vmbuilder')
    boot = is_found('{0}/boot.sh'.format(cdir))
    kcfg = is_found('{0}/vmbuilder.cfg'.format(cdir))
    kprt = is_found('{0}/vmbuilder.partitions'.format(cdir))

    makekvm(name, cdir, ipv4, kcfg, kprt, ddir)


def makekvm(kvm, cdir, ip, conf, part, ddir):
    """Builds the KVM. """
    mac = macaddress()
    configs = '-c {0} --part {1}  -d {2}/{3}'.format(conf, part, ddir, kvm)
    network = '--hostname {0} --ip {1} --mac {2}'.format(kvm, ip, mac)
    vmbuild = '/usr/bin/vmbuilder kvm ubuntu -o -v {0} {1}'.format(network, configs)

    try:
        os.system(vmbuild)
    except VMBuilder.exception, e:
        print '[ERROR]: {0}'.format(e)
        sys.exit(1)

    print '\n\n-------------------------------------------'
    print 'KVM name:        {0}'.format(kvm)
    print 'Using template:  {0}'.format(cdir)
    print 'KVM destination: {0}'.format(ddir)
    print 'KVM IP address:  {0}'.format(ip)
    print '-------------------------------------------\n\n'
