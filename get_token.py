import msal

TENANT_ID = "a4c157c5-6383-41b4-8069-884c84c5fc6d"
CLIENT_ID = "daf9757e-4639-41fe-abf3-89e19b41ee86"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["api://9af8581c-30fc-4651-8273-cce1b22f46c6/.default"]

app = msal.PublicClientApplication(
    CLIENT_ID,
    authority=AUTHORITY
)

result = app.acquire_token_interactive(scopes=SCOPES)

if "access_token" in result:
    with open("aad_token.txt", "w") as f:
        f.write(result["access_token"])

    print("Token acquired successfully")
    print("Token saved locally")