# new-friend

This is a slackbot that can be trained on your slack history to emulate your friends and coworkers to great amusement for all.

It uses the https://github.com/jsvine/markovify library as core Markov chain functionality.

To install, clone the repo and run

`pip install .`

You'll need download the history from your slack. You can do this by following the instructions here:
https://slack.com/help/articles/201658943-Export-your-workspace-data

To train the markov model run

```bash
python3 -m new_friend train --data <export_data_path>
```

To run the model you need slack api keys in order to post to slack. 
<https://slack.com/help/articles/215770388-Create-and-regenerate-API-tokens>

The API token should be set in an environment variable called `SLACK_TOKEN`

```bash
python3 -m new_friend run --model model.p
```
