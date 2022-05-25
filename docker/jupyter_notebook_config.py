c.Application.log_level = 'INFO'
c.JupyterApp.log_level = 20
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.allow_root = True
c.NotebookApp.base_url = '/workshop/'
c.NotebookApp.local_hostnames = ['localhost', 'host.docker.internal']
c.NotebookApp.notebook_dir = '/opt/notebooks'
c.NotebookApp.port = 8000
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' http://* https://*"
    }
}
c.NotebookApp.trust_xheaders = True 
c.NotebookApp.ip = '*'
