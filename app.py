from slack_bolt import App
app = App()

@app.command("/<your_bot_name>")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>, you can get to <your_bot_name> from <https://your_bot_deep_link|here>!")

if __name__ == "__main__":
    app.start(3000)
