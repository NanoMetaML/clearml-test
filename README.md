# ClearML Test Repo

This is a quick test to verify you have a working clearml setup.

Verifying User:
1. Go to your ClearML WebApp Settings.
2. Under the WORKSPACES section, go to App Credentials, and click + Create new credentials
3. Copy your credentials
4. Add the code below to your code
```
   web_server = 'https://app.clear.ml' 
   api_server = 'https://api.clear.ml'
   files_server = 'https://files.clear.ml'
   access_key = 'FILL ACCESS KEY HERE'
   secret_key = 'FILL SECRET KEY HERE'
   
   
   Task.set_credentials(web_host=web_server,
                        api_host=api_server,
                        files_host=files_server,
                        key=access_key,
                        secret=secret_key
                        )
```
  

Running Task:
1. Clone this repository
2. Submit task to queue

   `clearml-task --name test --project clearml-test --script test.py --queue default`

