import os
from slackclient import SlackClient
print('getting slack token')
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
print(SLACK_TOKEN)
print('running...')
slack_client = SlackClient('xoxb-169102232896-Akgp4do1NACeD7lQWhZrpgfC')
test = slack_client.api_call("api.test")
print(test);

auth_test = slack_client.api_call("auth.test")
print(auth_test)
print('done')

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call['ok']:
        return channels_call['channels']
    return None


def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None


if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
            detailed_info = channel_info(c['id'])
            if detailed_info:
            	print('has details')
    else:
        print("Unable to authenticate.")

