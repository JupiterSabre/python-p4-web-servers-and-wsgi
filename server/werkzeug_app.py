#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

# ^^This is the sole function of the script. You can call it anything, (application in this case). It is decorated with the Request.application method, which tells it to run any code inside of the function in the browser at the location we specify with our development server.

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )

# ^^ The run_simple method runs a server for a one page application without complications. It is not suited for a production server that supports millions of users, but it gives us the tools we need to develop new pages for the web applications that we eventually deploy to those servers. 
        # ^^ run_simple requires three arguments: a host name (generally localhost), a port, and an application. This application will be defined in a function somewhere in the file. As we saw before, we named this one 'application'.