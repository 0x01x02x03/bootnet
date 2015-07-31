import sys, json, urllib3, certifi

shodan_keyfile = open("shodan.key", "r");
shodan_key = shodan_keyfile.read().strip();
shodan_url = "https://api.shodan.io/shodan/"

if len(sys.argv)>1:
	request_url = shodan_url+"host/count?key="+shodan_key+"&query="+sys.argv[1]
	h = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
	r = h.request("GET", request_url)
	j = json.loads(r.data.decode())
	print(j["total"])
	
else:
	print("Usage %s <search query>" % sys.argv[0]);
