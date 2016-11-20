## Simple crawler

### Configure your crawler

- create twitter app to access Twitter Streaming API (https://apps.twitter.com)
- create a file called *config.py* take example on *config.py.example*
- obtain and provide tokens and keys
- specify the database to write to (in this case it is expecting mongodb configurations)

### Get Started

1. Install virtualenv

  ```
  pip install virtualenv
  ```

2. Create an instance of virtualenv venv

  ```
  virtualenv venv
  ```

3. use the virtualenv

  ```
  source venv/bin/activate
  ```

4. Install the dependencies

  ```
  pip install -r requirements.txt
  ```
