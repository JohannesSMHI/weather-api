"""
TEMPLATE: https://github.com/sharksmhi/microservice_template

Examples:
    get: http://localhost:5000/translation
    get: http://localhost:5000/translation?attribute=WINDIR
    get: http://localhost:5000/translation?attribute=PROJ&value=BLK

"""
import connexion
from data_handler import DataHandler

handler = DataHandler()


def get_info(*args, attribute=None, value=None, **kwargs):
    """Get function."""
    return handler.get_info(
        attribute=attribute,
        value=value
    )


app = connexion.FlaskApp(
    __name__,
    specification_dir='../',
    options={'swagger_url': '/'},
)
app.add_api('openapi.yaml')

if __name__ == "__main__":
    app.run(port=5000)
