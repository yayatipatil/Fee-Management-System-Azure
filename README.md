# Fee Management System Using Azure

This project is a cloud-based fee management solution built using Microsoft Azure. It allows institutions to store student fee records, retrieve fee details, calculate payment status, update payments securely, and send overdue reminders through automated workflows.

## Overview

The system is designed to:
- Manage student and fee information in Azure SQL Database
- Expose secure APIs using Azure Functions
- Protect admin operations with Azure API Management and Microsoft Entra ID
- Send overdue fee reminders using Azure Logic Apps and Outlook
- Monitor application activity using Application Insights

## 1. Code and Configuration

The complete implementation files are already available in the repository. The project includes the following key artifacts:

- Azure Functions application:
  - azure-functions/db.py
  - azure-functions/function_app.py
  - azure-functions/host.json
  - azure-functions/requirements.txt
  - azure-functions/local.settings.json

- Database scripts:
  - database/create_tables.sql
  - database/sample_data.sql

- API Management policies:
  - apim-policy.xml
  - apim-update-fee-policy.xml
  - update-fee-policy.xml

- Token generation utility:
  - get_token.py

- Supporting files:
  - aad_token.txt
  - .gitignore

These files contain the complete Azure Functions code, database schema, sample data, and API policy settings used in the system.

## 2. Solution Architecture

Student / Admin
    |
    v
Azure API Management
    |
    v
Azure Functions
    |
    v
Azure SQL Database

Additional workflow:

Azure Logic App --> Azure SQL Database --> Outlook Email

Monitoring:

Application Insights monitors Azure Functions and API activity.

## 3. Key Azure Services Used

- Azure SQL Database: stores student fee and administrator data
- Azure Functions: handles fee retrieval and fee update operations
- Azure API Management: secures APIs and applies rate limits
- Microsoft Entra ID: validates administrator access tokens
- Azure Logic Apps: automates reminder emails for overdue fees
- Outlook: sends overdue payment notifications
- Application Insights: monitors performance and errors

## 4. Deployment Guide

### Step 1: Create Azure SQL Database
1. Create a new Azure SQL Database in the Azure portal.
2. Create the required tables by running the SQL script in database/create_tables.sql.
3. Insert sample records using database/sample_data.sql.

### Step 2: Configure the Function App
1. Create an Azure Function App using Python runtime.
2. Configure application settings:
   - AzureWebJobsStorage
   - FUNCTIONS_WORKER_RUNTIME
   - SQL_CONNECTION_STRING
3. Deploy the project files inside azure-functions.
4. Install the required Python packages from azure-functions/requirements.txt.

### Step 3: Configure API Management
1. Create an Azure API Management instance.
2. Import the Azure Functions endpoints into APIM.
3. Apply the policy files apim-policy.xml and apim-update-fee-policy.xml.
4. Set the backend URL to the deployed Azure Function endpoints.
5. Enable subscription key validation and rate limiting if required.

### Step 4: Secure Admin Updates with Entra ID
1. Register an application in Microsoft Entra ID.
2. Add required API permissions.
3. Validate the FeeAdministrator role in the API Management policy.
4. Use get_token.py to generate an access token for testing admin requests.

### Step 5: Configure Logic App for Reminders
1. Create a Logic App in Azure.
2. Set a recurrence trigger for daily execution.
3. Query Azure SQL for overdue students.
4. Send reminder emails through the Outlook connector.

### Step 6: Test the Solution
1. Test student fee lookup using the Azure Function endpoint.
2. Test payment status calculation.
3. Test admin fee update with a valid Entra token.
4. Check the database after updates.
5. Verify reminder emails are sent for overdue fees.

## 5. Security Notes

- Do not upload real credentials or tokens to GitHub.
- Store SQL connection strings and secrets in Azure App Settings or Azure Key Vault.
- Use APIM subscription keys and Entra ID validation for secure access.
- Restrict fee update access to authorized administrators only.

## 6. Summary

This project demonstrates a practical Azure-based fee management workflow that combines secure APIs, database-driven fee tracking, role-based admin access, and automated reminder notifications.
