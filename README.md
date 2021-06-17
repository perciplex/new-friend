# new-friend

This is a slackbot that can be trained on your slack history to emulate your friends and coworkers to great amusement for all.

It uses the https://github.com/jsvine/markovify library as core Marjov chain functionality.

To install, clone the repo and run

`pip install .`

You'll need download the history from your slack. You can do this by following the instructions here https://slack.com/help/articles/201658943-Export-your-workspace-data

To train the markov model run

```bash
python3 -m new_friend train --data <export_data_path>
```

To run the model you need slack api keys in order to post to slack. 

```bash
python3 -m new_friend run --model model.p
```
