#!/usr/bin/env python3
import os
import sys
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler as CGIHandler


def display_server_info(port):
    main_module_dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
    fmt = "{}:\n\t{}"
    print("Server info:")
    print(fmt.format("Server's root directory", main_module_dirname))
    print(fmt.format("Server's CGI directories", CGIHandler.cgi_directories))
    print(fmt.format("Starting HTTP Server on port", port))


def configure_server():
    os.chdir("/home/kyleaubuchon/python/pythonlabs/examples/webservers/home")  # Specifiy the root directory of the server
    port = 8000 + os.getuid()
    return HTTPServer(('localhost', port), CGIHandler)
