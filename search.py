import shodan

shodan_keyfile = open("shodan.key", "r");
shodan_key = shodan_keyfile.read().strip();
shodan_api = shodan.Shodan(shodan_key);

try:
	results = shodan_api.search("apache");
	print('Results found: %s' % results['total']);

except(shodan_api.APIError, e):
	print('Error: %s' % e);

