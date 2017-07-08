.PHONY: test clean save

clean:
	rm -rf test

save:
	boilr template save . python -f

test: clean save
	boilr template use python ./test


