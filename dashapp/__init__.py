from dashapp import app1
from dashapp import app2

def register_dashapps(server):
    app1.register_dash(server)
    app2.register_dash(server)
