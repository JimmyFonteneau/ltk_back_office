from .base import *

os.environ.setdefault('ENVIRONMENT', 'dev')

if os.environ['ENVIRONMENT'] == 'prod':
   from .prod import *
else:
   from .dev import *