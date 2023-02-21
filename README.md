# FEB 14 2023 UPDATE: Deta Cloud moved to Deta Space
This guide is partially broken. The code still works but the steps for deploying/hosting is different. Use https://github.com/imptype/deta-space-fastapi-example for the updated steps, and you'll need to modify the `Spacefile` to include the environment variables (check the [docs](https://deta.space/docs/en/reference/spacefile)).

## Information
This is an interactions-only discord bot hosted on [Deta](https://deta.sh). Its purpose is to serve a basic leaderboards system.

## Commands
An asterisk (*) means staff can only use it.
- `/ping` - pings the bot.
- `*/1v1 <winner> <loser>` - winner awarded 5 points and loser deducted 5 points.
- `*/setpoints <user> <points>` - gives the user points.
- `/getpoints <user>` - views the user's points.
- `*/getall` - views everyone's points, in descending order, capped at 4000 characters.

## Running the bot
1. Make a new project on [Deta](https://web.deta.sh/home).
2. Make a new application on [Discord](https://discord.com/developers/applications).
3. Click the 'Deploy to Deta' button on this repo.
4. Select your project and enter the environment variables.
  - `CLIENT_ID` is the ID in https://discord.com/developers/applications/{id}/information
  - `CLIENT_PUBLIC_KEY` is the key in https://discord.com/developers/applications/{id}/information
  - `CLIENT_SECRET` is the secret in https://discord.com/developers/applications/{id}/oauth2/general
  - `STAFF_ROLE_ID` is the ID of a staff role in the discord server.
5. Once deployed, visit this page of the Micro's URL [https://{id}.deta.dev/update_commands](https://deta.sh) to register the slash commands for the first time.
6. Set the `Interactions Endpoint URL` to [https://{id}.deta.dev/discord](https://deta.sh) in https://discord.com/developers/applications/{id}/information.

Refresh Discord if the slash commands don't show up immediately.

## Deploy
Click the following button to deploy this Micro in your own Deta project:

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy)
