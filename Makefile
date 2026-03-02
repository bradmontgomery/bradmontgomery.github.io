SITE := uvx --from git+https://github.com/bradmontgomery/site site

.PHONY: build new server

build:
	$(SITE) build

new:
	$(SITE) new

server:
	$(SITE) server
