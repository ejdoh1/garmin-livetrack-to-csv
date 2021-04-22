# Garmin LiveTrack JSON to CSV API
 
Converts a Garmin LiveTrack JSON feed to CSV for livestream video overlay integration.

To use, get a Garmin activity session ID poll https://abc.execute-api.ap-southeast-2.amazonaws.com/dev/session/REPLACE_ME_SESSION_ID every 5s or so.

## Deploy

```sh
# update/remove profile in serverless.yml
# start docker
npm i
sls deploy
```
