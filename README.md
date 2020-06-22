
# LHA

Voice recognition for education systems​

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install LHA dependecies.

```bash
pip install pipenv
pipenv install
```

## Environment Variables
To use the google API, you need to follow [these steps](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries)
to get a valid key.
After it, you must add it as an environment variable:

GOOGLE_APPLICATION_CREDENTIALS=[PATH_TO_KEY]

## Usage

```bash
venv/bin/python src/LHA.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
