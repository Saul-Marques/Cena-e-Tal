import pusher

pusher_client = pusher.Pusher(
  app_id='1948918',
  key='9505bbfcec175b686952',
  secret='d82d37c90e27fc1b17b8',
  cluster='eu',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})