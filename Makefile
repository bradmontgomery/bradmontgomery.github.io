SITE := uvx --from git+https://github.com/bradmontgomery/site site

.PHONY: build new server

build:
	$(SITE) build --content content --output docs

new:
	$(SITE) new

server:
	$(SITE) server --addr 127.0.0.1 --port 9000 --output docs
