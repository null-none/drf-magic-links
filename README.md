# drf-magic-links

## Installation

```bash
pip install drf-magic-links
```

Add URL patterns

```
# urls.py

from django.urls import path

urlpatterns = [
    path('/api/', include('magic_links.urls.api')),

    ...
]
```

Override settings as needed

```
# settings.py

MAGIC_LINKS = {
    # URLS for creating links, dict key corresponds to `source` when requesting link
    'MAGIC_LINKS_URLS': {
        'default': 'http://localhost:8000/auth/',
        'ios': 'myapp://login/',
    },

    # Amount of time that tokens last, in seconds
    'MAGIC_LINKS_EXPIRE_TIME': 15 * 60,

    # Registers previously unseen aliases as new users.
    'MAGIC_LINKS_CREATE_USER': True,

    # The user's email field name
    'MAGIC_LINKS_USER_EMAIL_FIELD_NAME': 'email',

    # The email the callback token is sent from
    'MAGIC_LINKS_EMAIL_FROM_ADDRESS': 'from@example.com',

    # The email subject
    'MAGIC_LINKS_EMAIL_SUBJECT': "Your Magic Link",

    # A plaintext email message overridden by the html message. Takes one string.
    'MAGIC_LINKS_EMAIL_PLAINTEXT_MESSAGE': "Follow this link to sign in: {link}",

    # The email template name.
    'MAGIC_LINKS_EMAIL_HTML_TEMPLATE_NAME': 'magic_link_email.html',

    # Context Processors for Email Template
    'MAGIC_LINKS_CONTEXT_PROCESSORS': [],
}

```

## Example Usage

### REST API

```bash
curl -X POST -d “email=test@test.com&source=ios” localhost:8000/api/auth/email/
```

The user test@test.com receives an email

```
    Follow this link to sign in: myapp://login/?token=$2b$12$Pc9ugN5DwsC3jNYwpfG.XOxUuwybmJu1HTvfpPCyGk/I3BkFLZDsq&email=drwho@tardis.com
```

At this point, the client can use the supplied token to request a DRF auth token

```bash
curl -X POST -d “email=test@test.com&token=$2b$12$Pc9ugN5DwsC3jNYwpfG.XOxUuwybmJu1HTvfpPCyGk/I3BkFLZDsq” localhost:8000/api/auth/token/

{
    "token": "3d247ac9a67630932bb6b5e08cb24c0c7760f37a"
}
```
