from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

PROJECT_ENDPOINT="https://<your-foundry-resource>.services.ai.azure.com/api/projects/<your-project>"
AGENT_NAME="IT-HelpDesk-Agent"

client=AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

openai=client.get_openai_client()

response=openai.responses.create(
    extra_body={"agent_reference":{"name":AGENT_NAME,"type":"agent_reference"}},
    input="How do I reset my company password?"
)

print(response.output_text)