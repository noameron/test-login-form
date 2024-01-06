from enum import Enum


class GmailCreds(Enum):
    EMAIL_ADDRESS = 'noameron3'
    EMAIL_ADDRESS_WRONG_DOMAIN = 'noameron3'
    BAD_EMAIL_ADDRESS = 'bad_email'
    BAD_EMAIL_ADDRESS_SPECIAL_CHARS = 'bad_email@#$%^&*()'
    BAD_PASSWORD = '1234'


class ErrorMessages(Enum):
    BAD_EMAIL_ADDRESS = "Couldn’t find your Google Account"
    NOT_VALID_EMAIL_ADDRESS = "Enter a valid email or phone number"
    NO_PASSWORD = "Enter a password"
    BAD_PASSWORD = "Wrong password. Try again or click Forgot password to reset it."

