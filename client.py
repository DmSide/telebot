from telethon import TelegramClient
# from telethon.errors.rpc_errors_401 import SessionPasswordNeededError
from telethon.tl.functions import messages
from telethon.tl.types import InputPeerEmpty, PeerChannel, PeerChat, PeerUser, Dialog, DialogPeer, InputPeerChat, \
    InputPeerChannel, InputPeerUser
from tele_key import api_id, api_hash
import asyncio
# (1) Use your own values here

phone = '+79604444815'
username = 'SideCopier'


async def create_client(number):
    return await TelegramClient(number, api_id, api_hash).connect()


async def ass_get_me():
    return await client.get_me()


async def ass_get_dialogs():
    get_dialogs = messages.GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=30,
        hash=61617
    )
    return await client(get_dialogs)

with TelegramClient(username, api_id, api_hash) as client:
    client.send_message('me', 'Hello, myself!')
    client.connect()

    client2 = create_client(username)

    # Ensure you're authorized
    if not client.is_user_authorized():
        client.send_code_request(phone)
        try:
            client.sign_in(phone, input('Enter the code: '))
        except EnvironmentError: # SessionPasswordNeededError:
            client.sign_in(password=input('Password: '))

    me = client.get_me()
    print(me)

    dialogs = ass_get_dialogs()
    print(dialogs)
    #
    # get_history = messages.GetHistoryRequest(
    #     peer=InputPeerEmpty(),
    #     offset_id=0,
    #     offset_date=None,
    #     add_offset=0,
    #     limit=50,
    #     max_id=9999999,
    #     min_id=0,
    #     hash=61617
    # )
    # dialogs = client(get_history)
    # print(dialogs)

    counts = {}

    # create dictionary of ids to users and chats
    users = {}
    chats = {}

    for u in dialogs.users:
        users[u.id] = u

    for c in dialogs.chats:
        chats[c.id] = c

    for d in dialogs.dialogs:
        peer = d.peer
        if isinstance(peer, PeerChannel):
            id = peer.channel_id
            channel = chats[id]
            access_hash = channel.access_hash
            name = channel.title

            input_peer = InputPeerChannel(id, access_hash)
        elif isinstance(peer, PeerChat):
            id = peer.chat_id
            group = chats[id]
            name = group.title

            input_peer = InputPeerChat(id)
        elif isinstance(peer, PeerUser):
            id = peer.user_id
            user = users[id]
            access_hash = user.access_hash
            name = user.first_name

            input_peer = InputPeerUser(id, access_hash)
        else:
            continue

        get_history = messages.GetHistoryRequest(
            peer=input_peer,
            offset_id=0,
            offset_date=None,
            add_offset=0,
            limit=1,
            max_id=0,
            min_id=0,
        )

        history = client(get_history)
        if isinstance(history, Messages):
            count = len(history.messages)
        else:
            count = history.count

        counts[name] = count

    print(counts)