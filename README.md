# AI-103 course code

Code for the Cloudxeus course **AI-103: Azure AI Apps and Agents Developer Associate**. Each folder
is one section of the course, under the same name you see in the videos.

| Section |
|---|
| 01. Building the Foundation Models, Tools, and the Developer Workflow |
| 02. From Prompts to Agents Building RAG and Agentic Solutions on Microsoft Foundry |
| 03. Production-Ready AI Memory, Workflows, Monitoring, and Safety |
| 04. The Wider Ecosystem LangChain, LangGraph, and the Model Context Protocol |
| 05. Implement computer vision solutions |
| 06. Implement text analysis solutions |
| 07. Implement information extraction solutions |
| 08. Capstone Project Overview Building the CloudXeus AI Course Assistant |

## Before you start

You need:

- Python 3.13
- An Azure subscription
- The [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli), signed in with `az login`
- [Azure Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local), for the Azure Functions folders in sections 02 and 04

## Run a section

Each section has its own `requirements.txt`, so give each its own virtual environment. On Windows:

```powershell
cd "01. Building the Foundation Models, Tools, and the Developer Workflow"
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On macOS or Linux, activate it with `source .venv/bin/activate`. The Azure Functions folders
(`11. cloudxeus-func`, `12. cloudxeus-func1` and `03-cloudxeus-mcp`) have their own `requirements.txt`.
For those, also copy `local.settings.sample.json` to `local.settings.json`.

## Use your own Azure resources

The videos show the instructor's Azure resources. Here, those names are placeholders in angle
brackets, and blank settings such as `api_key=""` are for your own keys. Replace them before you run
a file, including the angle brackets:

| Placeholder | Replace with |
|---|---|
| `<your-foundry-resource>`, `<your-capstone-foundry-resource>` | Your Microsoft Foundry resource's name |
| `<your-project>` | Your Foundry project's name |
| `<your-search-service>`, `<your-capstone-search-service>` | Your Azure AI Search service's name |
| `<your-content-safety-resource>`, `<your-capstone-content-safety-resource>` | Your Azure AI Content Safety resource's name |
| `<your-capstone-document-intelligence-resource>` | Your Document Intelligence resource's name |
| `<your-capstone-storage-account>` | Your storage account's name |
| `<your-function-app>` | Your Azure Function App's name |
| `<your-subscription-id>`, `<your-resource-group>` | Your subscription ID and resource group |

Model deployment names in the code also need to match your own deployments.

## Keep your keys safe

**Never commit or share a file with your key in it.** Anyone who gets your key can run up charges on
your Azure subscription.

- Before you commit or push your own copy, set any keys back to `""`.
- If a key does get out, regenerate it in the Azure portal straight away. Deleting the file isn't enough.
- `local.settings.json` and `.env` are already in `.gitignore`. Don't remove them.

## Azure costs

These labs create Azure resources that can cost money while they exist. Delete what you created when
you finish, usually by deleting its resource group.

## License

[MIT](LICENSE). The code is provided as is, as learning material.
