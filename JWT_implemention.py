"""
This is one layer down implementation of JWT token generation and verification
using SHA-256 and Base64URL 
"""
import base64
import hashlib
import secrets
import json
import hmac

class JWT:
    SECRET_KEY = 'b94b18b52eb3d278da4f50a478cce83171474e1d7341d5efa106eab1b7224454497d43753a63ccdcb68c35a630bf1762d22d97f36df788a4f5d023b8e4a97357b2e4995dd61ee5c416629a0392d498bf7342ad986f7cf17096e92098a74faf0133a9593b89b8c2e933c7c5869084bebdadd97e7fb7433566db243cecb30f5d1d698be6474ae48a513e94b45634ab602ec79108aa2adeb6e9b261bbb7ebc571db9183ba6461235fbd1f9397957212d148682355e954b7bc7b2ffef528e14d23942f621399e25cf53320cae6f85a09969cdbe8245898f0d1e1928e5691cc3143cc9c16a4ec21aec7ce428051cdce7bca59012fa9a6559495a215dd69c5aaa74ad9'

    def __init__(self, encoded_header, encoded_payload, signature):
        self.encoded_header = encoded_header
        self.encoded_payload = encoded_payload
        self.signature = signature
        
    @classmethod
    def encode(cls, payload:str, header:dict={'alg':'HS256','typ':'JWT'}):
        header_json = json.dumps(header).encode('utf-8')
        payload_json = json.dumps(payload).replace(', ',',').replace(': ',':')
        print(payload_json)
        payload_json = payload_json.encode('utf-8')
        encoded_header = base64.b64encode(header_json)
        encoded_payload = base64.b64encode(payload_json)
        signature = (
            encoded_header + b'.' +
            encoded_payload
        )
        signature = hmac.new(
            cls.SECRET_KEY.encode('utf-8'),
            signature,
            hashlib.sha256
            ).hexdigest()
        
        return cls(encoded_header.decode(), encoded_payload.decode(), signature)
    
    def __str__(self) -> str:
        return f'{self.encoded_header}.{self.encoded_payload}.{self.signature}'


payload = {
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
x = JWT.encode(payload)
print(x)