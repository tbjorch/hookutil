# hookutil
A hook util written in Python allowing the user to run pre-uploaded shellscripts on a server upon web calls. It's a simple hook service which only provides a simple way of authenticate the calls by using an API Key.

# Guide
## Setup
Make sure to add your own API key to add some level of authentication on the calls and **keep the key secret**

## Add scripts
1. Put your shellscript into the scripts directory
2. Add the following metadata about the script into the scripts.ini configuration file:
  - **[NAME]** of the script to be called in the web call
  - **log_message** sent to the log whenever the script is executed
  - **file_name** of the script file in the scripts directory

## Call hook
1. Send a post request to the api on port 5959 (e.g. http://localhost:5959/)
2. In the request body, add json data formatted as the below. Make sure the script value matches the name in your scripts.ini file of the script you want to run
```JSON
{
  "APIKey": "mySuperSecretApiKey",
  "script": "helloworld",
  "args": ["list", "of", "arguments", "for", "shell", "script"]
}
```
