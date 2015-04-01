# -*- coding: utf-8 -*-

import requests
import uuid

def sendMsg(url, sender, pwd, msg, receivers, session=None):
	if not session:
		session = "{%s}" % str(uuid.uuid1())
	msg = msg.encode("gbk")
	params = {"sender":sender,"pwd":pwd,"msg":msg,\
		"receivers":";".join(receivers),"sessionid":session}

	resp = requests.post(url,data=params)
	return resp.ok

if __name__ == '__main__':
	import sys
	print(sys.argv, len(sys.argv))
	if len(sys.argv) < 7:
		raise Exception("pls specify:[url, sender, pwd, msg, session, receivers]")
	url = sys.argv[1]
	sender = sys.argv[2]
	pwd = sys.argv[3]
	msg = sys.argv[4]
	session = sys.argv[5]
	receivers = sys.argv[6:]

	try:
		uuid.UUID(session)
	except Exception, e:
		session = None

	sendMsg(url, sender, pwd, msg, receivers, session)


