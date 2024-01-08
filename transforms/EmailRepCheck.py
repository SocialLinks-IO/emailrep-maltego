from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform

import asyncio
import json
import requests

API_KEY = ""
TEST_MODE = False

TAGS = [
    "blacklisted",
    "malicious_activity",
    "malicious_activity_recent",
    "credentials_leaked",
    "credentials_leaked_recent",
    "data_breach",
    "domain_exists",
    "new_domain",
    "suspicious_tld",
    "spam",
    "free_provider",
    "disposable",
    "deliverable",
    "accept_all",
    "valid_mx",
    "spoofable",
    "spf_strict",
    "dmarc_enforced",
]

class EmailRepCheck(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        email = request.getProperty("email")

        if not TEST_MODE:
            data = requests.get(
                f'https://emailrep.io/{email}',
                headers = {
                    'Key': API_KEY,
                    'User-Agent': 'Emailrep Maltego Transform',
                }
            ).json()
        else:
            data = json.load(open('transforms/bill.json'))


        if data.get('status') == 'fail':
            response.addEntity('maltego.Tag', data.get('reason', 'Emailrep request error'))
            return

        details = data['details']

        first_seen = response.addEntity("maltego.date", details.get('first_seen'))
        first_seen.setLinkLabel('First seen')

        last_seen = response.addEntity("maltego.date", details.get('last_seen'))
        last_seen.setLinkLabel('Last seen')

        response.addEntity('maltego.MXRecord', details.get('primary_mx')).setLinkLabel('MX Record')
        response.addEntity('maltego.Phrase', f"{data.get('references')} references").setLinkLabel('Count of references of email address')
        response.addEntity('maltego.Phrase', f"{details.get('days_since_domain_creation')} days since domain creation").setLinkLabel('Days Since Domain Creation')
        response.addEntity('maltego.Sentiment', details.get('domain_reputation')).setLinkLabel('Domain reputation')
        response.addEntity('maltego.Sentiment', data.get('reputation')).setLinkLabel('Email reputation')

        suspicious = 'Suspicious' if data.get('suspicious') else f'Not Suspicious'
        response.addEntity('maltego.Tag', suspicious).setLinkLabel('Is suspicious')

        for profile in details.get('profiles'):
            response.addEntity('maltego.profile.exists', profile.title()).setLinkLabel('Registered in')

        for t in TAGS:
            value = t if details.get(t) else f'not {t}'
            tag = response.addEntity("maltego.Tag", value.title().replace('_', ' '))
            tag.setLinkLabel(t)
