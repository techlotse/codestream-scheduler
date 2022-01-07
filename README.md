# codestream-scheduler
vRealize Orchestrator Action to allow for Codestream Scheduling

Action require 4 Named String inputs:

vRealizeApplianceURL = FQDN of vRealize Automation Appliance (https://fqdn).
codestreamUserName = Username for vRealize Automation.
codestreamPassword = Password for the user (SecureString).
pipelineUUID = UUID of the pipeline to execute. Obtained from the URL in GUI.

The Action can then be used as part as a Scheduled Workflow in Orchestrator