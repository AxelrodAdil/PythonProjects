import socket


def get_ip_by_host_name():
    hostname = input('URL? ')
    try:
        return f'Hostname: {hostname}\nIP: {socket.gethostbyname(hostname)}'
    except socket.gaierror as error:
        return f'Invalid Hostname - {error}'


def main():
    print(get_ip_by_host_name())


if __name__ == '__main__':
    main()
