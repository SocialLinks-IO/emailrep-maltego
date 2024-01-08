# Emailrep transform for Maltego

A free transform to get a reputation of an email address in a second with **the power of [emailrep.io](emailrep.io)**.

<img width="700" alt="Success" src="https://github.com/soxoj/emailrep-maltego/assets/31013580/e2db720f-a2a7-46cc-9a1b-ec7ae6ec48d4">

# Installation

## Create transform

1. Press "New Local Transforms..." button

<img width="453" alt="Step 1" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/72047edc-a666-4aa2-8cee-9a49fd643066">

2. Fill in the fields in the first window

<img width="860" alt="Step 2" src="https://github.com/soxoj/emailrep-maltego/assets/31013580/fdb22628-7794-41d1-8fdf-74318dff253c">


3. Fill in the fields in the second window

<img width="860" alt="Step 3" src="https://github.com/soxoj/emailrep-maltego/assets/31013580/de43d938-31d4-4e09-96a2-b4c1b3eeb1c4">

4. It's not necessary but for the correct display of entities I recommend installing SocialLinks Pro entities from the Maltego Hub, that's free.

## API key

It's not necessary (read below), but in case you have an API key, put it in [transforms/EmailRepCheck.py](transforms/EmailRepCheck.py) file.

```python
API_KEY = "YOU-KEY-HERE"
```

# Usage

emailrep.io has a quite low limit without an API key. You can request a [free API key](https://emailrep.io/key) (10 requests per day, 250 per month) or buy Commercial / Enterprise access.

Create an Email entity and launch the transform!

<img width="998" alt="Success" src="https://github.com/soxoj/emailrep-maltego/assets/31013580/e2db720f-a2a7-46cc-9a1b-ec7ae6ec48d4">

A message about exceeding limits looks like:

<img width="311" alt="Fail" src="https://github.com/soxoj/emailrep-maltego/assets/31013580/a4dcb9f7-7f52-4dfe-9390-aac1ffd8abfd">
