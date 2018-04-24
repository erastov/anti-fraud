import pusher


class Pusher(object):

    pusher_client = pusher.Pusher(
      app_id='509691',
      key='16b0026a0399f224c710',
      secret='4b7e587592574869093d',
      cluster='eu',
      ssl=True
    )

    def send_message(self, message):
        self.pusher_client.trigger('my-channel', 'my-event', {'message': message})
