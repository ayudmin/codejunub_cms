import os
import dotenv

from django.core.wsgi import get_wsgi_application


dotenv.load_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Coming_soon.dev')

if os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')
    project_environment = os.environ['DJANGO_SETTINGS_MODULE']

env = project_environment
application = get_wsgi_application()
