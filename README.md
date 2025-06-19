
#  Intelligent PDF Summarizer

This project demonstrates a serverless, event-driven application that uses **Azure Durable Functions**, **Blob Storage**, and (optionally) **Azure Cognitive Services** to summarize PDF files uploaded to Azure Blob Storage.

It is modeled after the official [Azure-Samples](https://github.com/Azure-Samples) implementation and fulfills the lab requirement for showcasing Durable Functions in a document processing scenario.

---

##  How It Works

1. A PDF is uploaded to the **\`input\`** container in Blob Storage.
2. A **Durable Function** is triggered by the blob upload.
3. The function reads the file and processes it.
4. *(Optional)* Text can be extracted using **Azure Form Recognizer**.
5. *(Optional)* The extracted content can be summarized using **Azure OpenAI**.
6. A summarized result is saved into the **\`output\`** container.

---

##  Technologies Used

- Azure Durable Functions (Python)
- Azure Blob Storage (Azurite emulator locally)
- Azure Storage Blob Trigger and Output Bindings
- (Optional) Azure Cognitive Services – Form Recognizer
- (Optional) Azure OpenAI
- Git & GitHub for version control

---

##  Running the App Locally

###  Prerequisites

- Python 3.9+
- [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- [Azurite](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite?tabs=visual-studio)
- [Azure Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer/)
- Visual Studio Code 

---

###  Setup Steps

1. **Start Azurite**
   \`\`\`bash
   azurite
   \`\`\`

2. **Create input/output containers using Azure Storage Explorer**
   - Right-click on \`Blob Containers\` → Create → \`input\`
   - Repeat → Create → \`output\`

3. **Create a virtual environment and install dependencies**
   \`\`\`bash
   python -m venv venv
   venv\\Scripts\\activate     # Use 'source venv/bin/activate' on Mac/Linux
   pip install -r requirements.txt
   \`\`\`

4. **Set up** `local.settings.json` at the root of your project:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "BLOB_STORAGE_ENDPOINT": "",
    "COGNITIVE_SERVICES_ENDPOINT": "",
    "AZURE_OPENAI_ENDPOINT": "",
    "AZURE_OPENAI_KEY": "",
    "CHAT_MODEL_DEPLOYMENT_NAME": ""
  }
}
```
5. **Start the Azure Function App**
 ```
   \`\`\`bash
   func start --verbose
   \`\`\`
```
6. **Upload a PDF to the input container**
   - Using Azure Storage Explorer: Right-click \`input\` → Upload
   - Or CLI:
     ```
     \`\`\`bash
     az storage blob upload \\
       --container-name input \\
       --file path/to/sample.pdf \\
       --name sample.pdf \\
       --connection-string "UseDevelopmentStorage=true"
     \`\`\` ```


7. **View output**
   - Switch to the \`output\` container and check for a \`.txt\` file containing the summary.

---



## youtube video

- https://youtu.be/Y44kk2lDvQw
---
