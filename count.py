import sys
import shodan

shodan_keyfile = open("shodan.key", "r");
shodan_key = shodan_keyfile.read().strip();
shodan_api = shodan.Shodan(shodan_key);

if len(sys.argv)>1:
	try:
		results = shodan_api.search(sys.argv[1]);
		print('Results found: %s' % results['total']);

	except (shodan.APIError, e):
		print('Error: %s' % e);

else:
	print("Usage %s <search query>" % sys.argv[0]);
