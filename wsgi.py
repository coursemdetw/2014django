#!/usr/bin/env python
import os
import imp
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append(os.path.join('wsgi', 'openshift'))

#
# Below for running on localhost
#
if __name__ == '__main__':
    ip   = 'localhost'
    port = 8051
    zapp = imp.load_source('application', 'wsgi/application')

    from wsgiref.simple_server import make_server
    httpd = make_server(ip, port, zapp.application)
    print("Django is running on:", ip, port)
    httpd.serve_forever()

