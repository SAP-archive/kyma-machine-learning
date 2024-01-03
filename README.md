![](https://img.shields.io/badge/STATUS-NOT%20CURRENTLY%20MAINTAINED-red.svg?longCache=true&style=flat)

# Important Notice
This public repository is read-only and no longer maintained. For the latest sample code repositories, visit the [SAP Samples](https://github.com/SAP-samples) organization.

# Hands-on Tutorial: Manage and Deploy Machine Learning Models in Kubernetes with SAP BTP, Kyma Runtime

## Description
This Github repository provides the basis material the Hands On blog, which covers the following main steps: 

1. Create an API endpoint which enables a user to create predictions on the fly with a trained machine learning model.
2. Containerize the Python script for our app in a Docker Image with all the needed requirements and dependencies.
3. Deploy and manage our container using Kubernetes in Kyma runtime, bringing the opensource world and SAP world together.

For further resources, go to:
GitHub: [Kyma Runtime Extension Samples](https://github.com/SAP-samples/kyma-runtime-extension-samples)

## Requirements
Running the sample requires access to the SAP Business Technology Platform (BTP) Kyma Runtime. There are also other sample-specific requirements that you can find in detail in the Hands-On blog. In summary the following software/editors are required: 

1. Python Editor like [Visual Studio](https://visualstudio.microsoft.com/de/vs/features/python/)
2. Kyma Runtime enabled [in the SAP BTP Trial](https://www.sap.com/cmp/td/sap-cloud-platform-trial.html)
3. [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
4. [Docker Hub Account](https://hub.docker.com/)
5. Command Line Tool like [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7.1)

## Download and Installation
The sample files can be downloaded and used within the respective user / developer environment, e.g. Python files may be opened and used within a Python Editor. The sample files don't require an installation step for themselves, they are simply downloaded and then opened in the respective editor. Through the dockerfile and the Python script the following Python libraries will be installed: 

1. Flask == 0.12.2
2. matplotlib == 3.2.2
3. numpy == 1.18.5
4. pandas == 1.0.5
5. requests == 2.24.0
6. scikit_learn == 0.23.1
7. seaborn == 0.10.1

## Known Issues
The sample is provided on the "as-is" basis. Currently, there are no known issues for the sample project.

## How to obtain support
The sample is provided "as-is". There is no guarantee that raised issues will be answered or addressed in future releases.

[Create an issue](https://github.com/SAP-samples/<repository-name>/issues) in this repository if you find a bug or have questions about the content. 
For additional support, [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

## License
Copyright (c) 2021 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
