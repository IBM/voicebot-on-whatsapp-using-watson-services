const twilioCredSubmit = document.getElementById("twilio-cred-submit");
const twilioStatus = document.getElementById("twilioStatus");
const waCredSubmit = document.getElementById("wa-cred-submit");
const waStatus = document.getElementById("waStatus");
const sttCredSubmit = document.getElementById("stt-cred-submit");
const sttStatus = document.getElementById("sttStatus");

twilioCredSubmit.onclick = () => storeTwilioCredentials();
waCredSubmit.onclick = () => storeWaCredentials();
sttCredSubmit.onclick = () => storeSttCredentials();

const storeTwilioCredentials = async () => {
    var url = '/storeTwilioCredentials';
    var payload = {
        account_sid: document.getElementById('account_sid').value,
        auth_token: document.getElementById('auth_token').value
    }
    var options = {
        method: 'post',
        body: JSON.stringify(payload)
    }

    console.log(options);

    await fetch(url, options).then(async (response) => {
        data = await response.json();
        console.log(data);
        getTwilioStatus();
        location.reload();
    });
};

const getTwilioStatus = async () => {
    await fetch('/getTwilioCredentials').then(async (response) => {
        data = await response.json();
        console.log(data);
        twilioStatus.innerHTML = data.status;
    });
};

const storeWaCredentials = async () => {
    var url = '/storeWaCredentials';
    var payload = {
        wa_apikey: document.getElementById('wa_apikey').value,
        wa_assistant_id: document.getElementById('wa_assistant_id').value,
        wa_url: document.getElementById('wa_url').value
    }
    var options = {
        method: 'post',
        body: JSON.stringify(payload)
    }

    console.log(options);

    await fetch(url, options).then(async (response) => {
        data = await response.json();
        console.log(data);
        getWaStatus();
        location.reload();
    });
};

const getWaStatus = async () => {
    await fetch('/getWaCredentials').then(async (response) => {
        data = await response.json();
        console.log(data);
        waStatus.innerHTML = data.status;
    });
};

const storeSttCredentials = async () => {
    var url = '/storeSttCredentials';
    var payload = {
        stt_apikey: document.getElementById('stt_apikey').value,
        stt_url: document.getElementById('stt_url').value
    }
    var options = {
        method: 'post',
        body: JSON.stringify(payload)
    }

    console.log(options);

    await fetch(url, options).then(async (response) => {
        data = await response.json();
        console.log(data);
        getSttStatus();
        location.reload();
    });
};

const getSttStatus = async () => {
    await fetch('/getSttCredentials').then(async (response) => {
        data = await response.json();
        console.log(data);
        sttStatus.innerHTML = data.status;
    });
};
