siab:
	sudo shellinaboxd -s /:LOGIN --disable-ssl \
			-f styles.css:static/shellinabox/style.css \
			-f ShellInABox.js:static/shellinabox/script.js \
			-f root_page.html:static/shellinabox/index.html \
			-f keyboard-layout.html:static/shellinabox/keyboard.html \
			-f index/:static/shellinabox/index.html \
			--localhost-only -d

uwsgi:
	uwsgi -s 127.0.0.1:1973 -w server:app

reset_database:
	python2.7 -c "from server import db; db.create_all()"
