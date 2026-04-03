import jwt

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhY2tlciIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNzc1MjQ3MTM1fQ.gDD9luHIQRi2gVs6Eyin4eVUt_-2VP1cXCbfH_yHMT4"

decoded_token = jwt.decode(token, options={"verify_signature": False})
print(decoded_token)