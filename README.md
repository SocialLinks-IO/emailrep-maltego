# Emailrep transform for Maltego

A free transform to get reputation of email address in a second.

# Installation

## Create transforms (manually)

Configure each file in transforms folder like this:

1. Press "New Local Transforms..." button

<img width="453" alt="Step 1" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/72047edc-a666-4aa2-8cee-9a49fd643066">

2. Fill in the fields in the first window

<img width="860" alt="Step 2" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/4cbc8be1-7b12-4dc3-bdcf-901d7816abd1">

3. Fill in the fields in the second window

<img width="860" alt="Step 3" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/1377825c-e63b-40ff-b8dd-031dc0752769">

It's not necessary but for correсt display of entities I recommend to install SocialLinks Pro entities from the Maltego Hub, that's free.

## API key

Put your API key in transforms/EmailRepCheck.py file.

```python
API_KEY = "YOU-KEY-HERE"
```

# Usage

emailrep.io has a quite low limit without API key. You can request a [free API key](https://emailrep.io/key) (10 requests per day, 250 per month) or buy Commercial / Enterprise access.

Create Email entity and launch the transform!