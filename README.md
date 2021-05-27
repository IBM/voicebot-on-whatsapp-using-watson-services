# voicebot-on-whatsapp-using-watson-services

Conversational AI VoiceBots are helping businesses automate repetitive, time-consuming queries and are giving your team more time to tackle more complex, high priority strategic tasks, while still ensuring that the customers are engaged. Chatbots that take in voice input can ingest, analyze, interpret, and respond to customer inquiries, with the end goal of either being able to answer a customer’s question in real-time or being able to continue a textual exchange with the customer to clarify the question at hand. 

In this code pattern, We will build a methodology using which the user will be able send his/her queries over voice on whatsApp and get a reply from Watson Assistant. The query from the user is sent to the Watson Speech to Text service through a custom application. The output from the Watson Speech to Text service is then feed to Watson Assistant. Watson Assistant replies back to the user with an appropriate reply. 

When you have completed this code pattern, you will understand how to:
* Use Watson Speech to Text service.
* Use Watson Assistant service.
* Integrate WhatsApp with Watson services.
* Handle queries sent over voice on WhatsApp. 

<!--add an image in this path-->
![architecture](doc/source/images/Architecture.png)

<!--Optionally, add flow steps based on the architecture diagram-->
## Flow

1. Step 1.
2. Step 2.
3. Step 3.
4. Step 4.
5. Step 5.

<!--Optionally, update this section when the video is created-->
# Watch the Video

<!-- [![video](http://img.youtube.com/vi/Jxi7U7VOMYg/0.jpg)](https://www.youtube.com/watch?v=Jxi7U7VOMYg) -->

# Pre Requisites

1. [IBM Cloud Account](https://cloud.ibm.com/registration): Create an IBM Cloud account.
2. [IBM Cloud CLI](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started&locale=en-US): Download and Install IBM Cloud CLI tool..
3. [OpenShift ROKS Cluster](https://cloud.ibm.com/kubernetes/catalog/create?platformType=openshift): Create an OpenShift Cluster.
4. [OC CLI](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html): Download and Install OpenShift CLI tool.
5. [Git Client](https://git-scm.com/downloads): Download Git Client CLI.

# Steps

1. [Clone the repo](#1-clone-the-repo)
2. [Create Watson Services](#2-create-watson-services)
3. [Build and Deploy the Python Application](#3-build-and-deploy-the-python-application)
4. [Create Twilio service](#4-create-twilio-service)
5. [Try out voicebot on WhatsApp](#5-try-out-voicebot-on-whatsapp)

### 1. Clone the repo

Clone the `/voicebot-on-whatsapp-using-watson-services` repo locally. In a terminal, run:

```bash
git clone https://github.com/IBM//voicebot-on-whatsapp-using-watson-services.git
```
We will be using the following directory:

- `python-application/` - To build and deploy the application.

### 2. Create Watson Services

Create the following Watson Services:
#### 2.1: Watson Speech to Text service
##### 2.1.1: Create service
<details><summary><b>IBM Cloud Pak for Data</b></summary>

- On Cloud Pak for Data, go to the **Service catalog** and deploy Watson Speech To Text Service, by clicking on the `Deploy` and following the instructions.
![Speech-to-text-service-cp4d](doc/source/images/stt-service-cp4d.png)
</details>

<details><summary><b>IBM Cloud</b></summary>

- On IBM Cloud, create a [Watson Speech To Text Service](https://cloud.ibm.com/catalog/services/speech-to-text), under `Select a pricing plan` select `Lite` and click on `create` as shown.
![Speech-to-text-service](doc/source/images/stt-service.png)
</details>

##### 2.1.2: Copy service credentials
- In Speech To Text Dashboard, Click on `Services Credentials`
![](doc/source/images/service-credentials.png)

- Click on `New credential` and add a service credential as shown. 
![](doc/source/images/create-stt-credentials.gif)

**NOTE:** Once the credential is created, copy and save the credentials in a text file for using it in later steps in this code pattern.

#### 2.2: Watson Assistant service
##### 2.2.1: Create service
<details><summary><b>IBM Cloud Pak for Data</b></summary>

- On Cloud Pak for Data, go to the **Service catalog** and deploy Watson Assistant Service by clicking on the `Deploy` and following the instructions.
![assistant-service-cp4d](doc/source/images/wa-service-cp4d.png)

</details>

<details><summary><b>IBM Cloud</b></summary>

- On IBM Cloud, create a [Watson Assistant Service](https://cloud.ibm.com/catalog/services/speech-to-text), under `Select a pricing plan` select `Lite` and click on `create` as shown.
![assistant-service](doc/source/images/wa-service.png)
</details>

##### 2.2.2: Copy credentials

- In Watson Assistant Dashboard, Click on `Services Credentials` and delete all the existing credentials. Create a new credential by clicking on `New credential`.
![](doc/source/images/wa-service-creds.png)

>Note: Deleting of existing credentials and creating a new service credentials is required because the `https://gateway-lon.watsonplatform.net` url is deprecated, on creating a new credential you should see an url like `https://api.eu-gb.assistant.watson.cloud.ibm.com`.

- In Watson Assistant Dashboard, Click on `Manage` and **Launch** the Watson Assistant.
![](doc/source/images/wa-assistant.png)

- Click on **Create assistant** and give your assistant a name and create it.
![](doc/source/images/create-assistant.png)

- In Assistant dashboard, under **Dialog** click on **add dilog skill**.
![](doc/source/images/create-dilog.png)

- Select **Upload skill** and upload the `skill-Portugues-Assistant-Skill.json` skill present in [`/watson-assistant-skill/`](watson-assistant-skill/) directory.
![](doc/source/images/upload-skill.png)

- In Assistant dashboard, click on the three dots and select **Assistant settings**.
![](doc/source/images/three-dots.png)

- Copy the `Assistant ID`, `Assistant URL` and `API key` as shown.
![](doc/source/images/wa-creds.png)

**NOTE:** Copy `Assistant ID`, `Assistant URL` and `API key` and save the credentials in a text file for using it in later steps in this code pattern.

### 3. Build and Deploy the Python Application

#### 3.1: Build
#### 3.2: Deploy

### 4. Create Twilio service

### 5. Try out voicebot on WhatsApp


## Summary

In this Code Pattern you learned how to create a WhatsApp Chatbot that take in voice input and get a reply from Watson Assistant. We used WhatsApp, Watson Speech to text, Watson Assistant and a custom python application to build this solution.


## Questions

If you have any questions or issues you can create a new [issue here](https://github.com/IBM/voicebot-on-whatsapp-using-watson-services/issues).

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make. For
example:

1. Fork the repo
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

This code pattern is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)
