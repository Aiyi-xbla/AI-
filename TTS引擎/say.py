import sys, json, http.client, winsound
c = http.client.HTTPConnection('127.0.0.1', 18765, timeout=300)
d = json.dumps({'text': sys.argv[1], 'emotion': sys.argv[2] if len(sys.argv) > 2 else 'NORMAL'})
c.request('POST', '/speak', d, {'Content-Type': 'application/json'})
p = json.loads(c.getresponse().read().decode()).get('file','')
if p: winsound.PlaySound(p, winsound.SND_FILENAME)
