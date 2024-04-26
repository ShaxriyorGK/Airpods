const express = require('express');
const bodyParser = require('body-parser');
const TelegramBot = require('node-telegram-bot-api');

var token = '7061132041:AAGn_ipGpipUdD3E99Wdj48-1S-6Ewp6m6w'

const app = express();
const bot = new TelegramBot(token, { polling: false });

app.use(bodyParser.json());

app.post('/send-message', (req, res) => {
    const message = req.body.message;

    // Send message to Telegram chat or bot
    bot.sendMessage('5612986349', message)
        .then(() => {
            res.sendStatus(200);
        })
        .catch((error) => {
            console.error('Error sending message:', error);
            res.sendStatus(500);
        });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
