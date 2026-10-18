from fnc_splus import SyncClient

if __name__ == '__main__':
    with SyncClient('personal', data_dir='sessions') as client:
        client.send('me', 'سلام از کلاینت همزمان')
