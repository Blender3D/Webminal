siab:
	sudo /usr/local/bin/shellinaboxd -s /:LOGIN --disable-ssl \
			-f styles.css:static/shellinabox/style.css \
			-f ShellInABox.js:static/shellinabox/script.js \
			-f root_page.html:static/shellinabox/index.html \
			-f keyboard-layout.html:static/shellinabox/keyboard.html \
			-f index/:static/shellinabox/index.html \
			--localhost-only -d

uwsgi:
	# gevent worker class: greenlet-based async I/O.
	# Concurrency = workers x worker-connections = 4 x 1000 = 4000 concurrent reqs.
	# (--threads is IGNORED with -k gevent; gevent uses greenlets, not threads.)
	# --max-requests 10000 = recycle each worker after ~10k requests (memory-leak defense).
	# --timeout 60       = kill stuck requests after 60s; raise only if a route legitimately needs longer.
	# --keep-alive 5     = reuse keep-alive connections from nginx for 5s (fewer TCP setups).
	# --log-level info   = production-appropriate (was: debug → ~95% extra log volume).
	gunicorn -k gevent \
		--workers 4 \
		--worker-connections 1000 \
		--max-requests 10000 \
		--max-requests-jitter 1000 \
		--timeout 60 \
		--keep-alive 5 \
		--log-level info \
		-b 127.0.0.1:1973 \
		server:app

reset_database:
	python2.7 -c "from server import db; db.create_all()"
