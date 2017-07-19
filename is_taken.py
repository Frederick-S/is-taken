import sys
import urllib.request


def is_taken(package_name):
    url = 'https://pypi.python.org/pypi/{0}'.format(package_name)

    try:
        with urllib.request.urlopen(url) as file:
            return True
    except urllib.error.HTTPError as http_error:
        if http_error.code == 404:
            return False
        else:
            print(http_error)

            sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: is-taken package-name")

    package_name = sys.argv[1]

    if is_taken(package_name):
        print("%s is taken" % package_name)
    else:
        print("%s is free to use" % package_name)
