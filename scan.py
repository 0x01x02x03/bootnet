import shodan

shodan_keyfile = open("shodan.key", "r");
shodan_key = shodan_keyfile.read().strip();
shodan_api = shodan.Shodan(shodan_key);


