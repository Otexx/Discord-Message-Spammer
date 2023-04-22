# Discord Token Spammer

<p align="center">
  <img src="https://img.shields.io/badge/language-Python-blue.svg">
</p>

1. Download this repository.
2. Add your Discord tokens to the `tokens.txt` file, one token per line.
3. Add the following JSON object to the `config.json` file, replacing `CHANNEL_ID` and `YOUR_MESSAGE_HERE` with your desired values:

   ```json
   {
       "channel_id": "CHANNEL_ID",
       "message": "YOUR_MESSAGE_HERE",
       "delay": 5,
       "threads": 4
   }
    ```
