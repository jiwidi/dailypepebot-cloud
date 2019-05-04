# Pepebot
[![Join Daily Qwertee on Telegram](https://patrolavia.github.io/telegram-badge/chat.png)](https://t.me/dailypepebot)
> Telegram bot that gives you random pepes under the command `/randompepe/`

A basic serverless [Telegram bot](https://core.telegram.org/bots) using [Google Cloud Functions](https://cloud.google.com/functions/).

This bot runs with Python 3.7 and [python-telegram-bot](https://python-telegram-bot.org/).

![](readmefiles/bot.png)

## Development setup

Fully serverless implementation with cloud functions on gcloud. The bot retrieves pepes tagged as approved from a g-datastore instance.

## Deployment

```
$ gcloud beta functions deploy webhook --set-env-vars "TELEGRAM_TOKEN=000:yyy" --runtime python37 --trigger-http
```
## TODOs
* The user should be able to set up a frequency to automatically recieve randompepes without the need to use /randomepep.
* Allow submitting pepes for later review and appending them to the master database.

## Release History

* 0.0.1
    * First release 

## Meta

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/jiwidi/dailypepebot-cloud](https://github.com/jiwidi/)

## Contributing

1. Fork it (<https://github.com/jiwidi/dailypepebot-cloud/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

