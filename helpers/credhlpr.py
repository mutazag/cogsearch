from azure.identity import (
    DefaultAzureCredential,
    EnvironmentCredential,
    ManagedIdentityCredential,
    SharedTokenCacheCredential,
    VisualStudioCodeCredential,
    AzureCliCredential,
    InteractiveBrowserCredential
)
from azure.core.exceptions import ClientAuthenticationError


def check_credential(credential_class, *args, **kwargs):
    try:
        credential = credential_class(*args, **kwargs)
        # Test the credential by getting a token
        token = credential.get_token("https://management.azure.com/.default")
        return f"✓ {credential_class.__name__} authentication succeeded"
    except Exception as e:
        return f"✗ {credential_class.__name__} authentication failed: {str(e)}"

