# Jupyter server configuration 

# Base log level.
c.Application.log_level = 'INFO'
c.JupyterApp.log_level = 20

# Allow the entry of requests from origin *.*.*.*
c.NotebookApp.allow_origin = '*'

# Allow remote access.
c.NotebookApp.allow_remote_access = True

# Allow to Jupyter of being executed by root user.
c.NotebookApp.allow_root = True

# Endpoint base path/url.
c.NotebookApp.base_url = '/workshop/'

# Local hostnames of the jupyter service is called within the container.
c.NotebookApp.local_hostnames = ['localhost', 'host.docker.internal']

# Noteboos directory.
c.NotebookApp.notebook_dir = '/opt/notebooks'

# Jupyter notebook service port.
c.NotebookApp.port = 8000

# Allow plotting using matplotlib within the notebooks. 
c.IPKernelApp.pylab = 'inline'

# Tornado service setting.
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' http://* https://*"
    }
}

# Allow headers accompanying the requests.
c.NotebookApp.trust_xheaders = True 

# IP that the Jupyter service will assume.
c.NotebookApp.ip = '*'
