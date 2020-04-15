# LHA

## Environment Variables
To use the google API, you need to follow [these steps](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries)
to get a valid key.
After it, you must add an it as environment variable:
   
GOOGLE_APPLICATION_CREDENTIALS=[PATH_TO_KEY]


## Usage
To get the action transcripted, you must send a request to this API.

###### POST /voice
```
{
    "audio": [path_to_file]
}
```