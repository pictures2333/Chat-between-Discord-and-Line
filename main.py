from flask import Flask
app = Flask(__name__)

import json, requests
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextSendMessage
from linebot.models import TextMessage, ImageMessage, VideoMessage, AudioMessage, LocationMessage, StickerMessage, FileMessage, ImageSendMessage
from imgurpython import ImgurClient
from datetime import datetime

with open('settings.json', 'r', encoding = 'utf-8') as f:
    d2 = json.load(f)

linebotapi = LineBotApi(d2["LineChannelAccessToken"])
handler = WebhookHandler(d2["LineChannelSecret"])

@app.route("/callback", methods = ['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        json_data = json.loads(body)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return("ok")

@app.route("/push_function/")
def home():
  try:
    msg = request.args.get('msg')
    if msg != None:
      linebotapi.push_message(d2['LineBotUserID'], TextSendMessage(text=msg))
      return msg
    else:
      return 'OK'
  except:
    print('error')
@app.route("/pimage/")
def home2():
  try:
    msg = request.args.get('msg')
    if msg != None:
        linebotapi.push_message(d2['LineBotUserID'], ImageSendMessage(original_content_url=msg, preview_image_url=msg))
        return msg
    else:
      return 'OK'
  except:
    print('error')

@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
    with open('request.json', 'r', encoding = 'utf-8') as f:
        d1 = json.load(f)
    print(event)
    d1['type'] = "LinePost"
    userid = str(event.source).replace('{"type": "user", "userId": "', '').replace('"}', '')
    profile = linebotapi.get_profile(userid)
    d1['content'] = f"{str(event.message.text)}"
    d1['header'] = f"[Line/{profile.display_name}]"
    d1['avatar'] = profile.picture_url
    d1['event'] = "textmsg"
    dumpdata = json.dumps(d1, ensure_ascii = False)
    with open(f'request.json', 'w', encoding = 'utf-8') as f:
        f.write(dumpdata)
    requests.get(f"{d2['LineWebhookUrl']}/push_function/?msg=[Line/{profile.display_name}]{str(event.message.text)}")

@handler.add(MessageEvent, message = StickerMessage)
def handle_message(event):
    with open('request.json', 'r', encoding = 'utf-8') as f:
        d1 = json.load(f)
    d1['type'] = "LinePost"
    userid = str(event.source).replace('{"type": "user", "userId": "', '').replace('"}', '')
    profile = linebotapi.get_profile(userid)
    stiii = json.loads(str(event.message))
    d1['event'] = f"sticker"
    d1['sticker'] = [stiii['packageId'], stiii['stickerId']]
    d1['header'] = f"[Line/{profile.display_name}]"
    d1['avatar'] = profile.picture_url
    dumpdata = json.dumps(d1, ensure_ascii = False)
    with open(f'request.json', 'w', encoding = 'utf-8') as f:
        f.write(dumpdata)
    requests.get(f"{d2['LineWebhookUrl']}/push_function/?msg=[Line/{profile.display_name}]<LINE STICKER PACKAGEID={d1['sticker'][0]} STICKERID={d1['sticker'][1]}>")

@handler.add(MessageEvent, message = ImageMessage)
def handle_message(event):
    with open('request.json', 'r', encoding = 'utf-8') as f:
        d1 = json.load(f)
    d1['type'] = "LinePost"
    userid = str(event.source).replace('{"type": "user", "userId": "', '').replace('"}', '')
    profile = linebotapi.get_profile(userid)
    image_content = linebotapi.get_message_content(event.message.id)
    image_name = event.message.id + '.jpg'
    path = image_name
    with open(path, 'wb') as fd:
        for chunk in image_content.iter_content():
            fd.write(chunk)
    requests.get(f"{d2['LineWebhookUrl']}/push_function/?msg=[Line/{profile.display_name}]<Picture Name={image_name}>")
    d1['event'] = f"image"
    d1['url'] = event.message.id + '.jpg'
    d1['header'] = f"[Line/{profile.display_name}]"
    d1['avatar'] = profile.picture_url
    dumpdata = json.dumps(d1, ensure_ascii = False)
    with open(f'request.json', 'w', encoding = 'utf-8') as f:
        f.write(dumpdata)
@handler.add(MessageEvent, message = VideoMessage)
def handle_message(event):
    with open('request.json', 'r', encoding = 'utf-8') as f:
        d1 = json.load(f)
    d1['type'] = "LinePost"
    userid = str(event.source).replace('{"type": "user", "userId": "', '').replace('"}', '')
    profile = linebotapi.get_profile(userid)
    video_content = linebotapi.get_message_content(event.message.id)
    path=event.message.id+".mp4"
    with open(path, 'wb') as fd:
        for chunk in video_content.iter_content():
            fd.write(chunk)
    requests.get(f"{d2['LineWebhookUrl']}/push_function/?msg=[Line/{profile.display_name}]<Video Name={path}>")
    d1['event'] = f"video"
    d1['url'] = event.message.id + '.mp4'
    d1['header'] = f"[Line/{profile.display_name}]"
    d1['avatar'] = profile.picture_url
    dumpdata = json.dumps(d1, ensure_ascii = False)
    with open(f'request.json', 'w', encoding = 'utf-8') as f:
        f.write(dumpdata)
@handler.add(MessageEvent, message = AudioMessage)
def handle_message(event):
    with open('request.json', 'r', encoding = 'utf-8') as f:
        d1 = json.load(f)
    d1['type'] = "LinePost"
    userid = str(event.source).replace('{"type": "user", "userId": "', '').replace('"}', '')
    profile = linebotapi.get_profile(userid)
    UserSendAudio = linebotapi.get_message_content(event.message.id)
    path = event.message.id + ".aac"
    with open(path, 'wb') as fd:
        for chunk in UserSendAudio.iter_content():
            fd.write(chunk)
    requests.get(f"{d2['LineWebhookUrl']}/push_function/?msg=[Line/{profile.display_name}]<Video Name={path}>")
    d1['event'] = f"audio"
    d1['url'] = event.message.id + '.aac'
    d1['header'] = f"[Line/{profile.display_name}]"
    d1['avatar'] = profile.picture_url
    dumpdata = json.dumps(d1, ensure_ascii = False)
    with open(f'request.json', 'w', encoding = 'utf-8') as f:
        f.write(dumpdata)

if __name__ == "__main__":
    app.run()