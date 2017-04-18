test: secrets clean
	python -m unittest discover -v -s tests

secrets: secrets.py

secrets.py:
	echo "Looks like you need to create the secrets.py file."
	exit 1

package: alexa_iapyx.zip

alexa_iapyx.zip: secrets.py iapyx.py
	rm -f alexa_iapyx.zip
	mkdir package
	cp secrets.py iapyx.py package/
	cp -a venv/lib/python2.7/site-packages/requests package
	cd package && zip -r ../alexa_iapyx.zip * && cd ..
	rm -rf package/

clean:
	rm -rf package/
	rm -f alexa_iapyx.zip
	rm -f *.pyc
	rm -f tests/*.pyc
