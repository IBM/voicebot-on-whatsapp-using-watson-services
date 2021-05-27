# voicebot-on-whatsapp-using-watson-services

Conversational AI VoiceBots are helping businesses automating repetitive, time-consuming queries and are giving your team more time to tackle more complex, high priority strategic tasks, while still ensuring the customers are engaged. Chatbots that take in voice input can ingest, analyze, interpret, and respond to customer inquiries spoken to them in natural language, with the end goal either being able to answer a customer’s question in real-time or continue a verbal exchange with the customer to clarify the question at hand. 

In this code pattern, We will build a methodology using which the user will be send his/her queries over voice on whatsApp and get a reply from Watson Assistant. The query from the user is sent to the Watson Speech to Text service through a custom application. The output from the Watson Speech to Text service is then feed to Watson Assistant. Watson Assistant replies back to the user with an appropriate reply. 

When you have completed this code pattern, you will understand how to:
* Use Watson Speech to Text service.
* Use Watson Assistant service.
* Integrate WhatsApp with Watson services.
* Handle queries sent over voice on WhatsApp. 

<!--add an image in this path-->
![architecture](doc/source/images/architecture.png)

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

### 2. Create Watson Services

Create the following Watson Services:
#### 2.1: Watson Speech to Text service

#### 2.2: Watson Assistant service

### 3. Build and Deploy the Python Application

#### 3.1: Build
#### 3.2: Deploy

### 4. Create Twilio service

### 5. Try out voicebot on WhatsApp


## Summary
In this Code Pattern you learned to create a chatbot using Watson Assistant which securely verifies user identity using SMS OTP authentication and interacts to display confidential information.


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
