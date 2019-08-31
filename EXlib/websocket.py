import json
from ws4py.client.threadedclient import WebSocketClient


class CG_Client(WebSocketClient):

    def opened(self):
        req = '{"event":"subscribe", "channel":"eth_usdt.deep"}'
        self.send(req)

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        # data = resp['data']
        # if type(data) is dict:
        #     ask = data['asks'][0]
        #     print('Ask:', ask)
        #     bid = data['bids'][0]
        #     print('Bid:', bid)
        print(resp)

if __name__ == '__main__':
    ws = None
    try:
        ws = CG_Client('ws://127.0.0.1:10086/api')
        ws.connect()

        # data={"msg": 10000,"msgId": 1}

        data={
  "msg": 11000,
  "msgId": 1,
  "data": {
    "id": 0,
    "text": "Hello this is control panel.",
    "choices": [
      "Open Baidu",
      "Open Google"
    ],
    "textFrameColor": 0x000000,
    "textColor": 0x56eeFF,
    "duration": -1
  }
}
        j=json.dumps(data)

        ws.send(j)
        ws.run_forever()

    except KeyboardInterrupt:
        ws.close()