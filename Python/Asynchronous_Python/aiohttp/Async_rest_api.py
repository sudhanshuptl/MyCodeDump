from aiohttp import web
import json


async def handler(requests):
    try:
        response = {'result': 'Dummy Response'}
        return web.Response(text=json.dumps(response), status=200)
    except Exception as e:
        response = {'error': 'Some Error Occur'}
        return web.Response(text=json.dumps(response), status=404)


async def new_user(requests):
    try:
        usr = requests.query['name']
        print('New User created :', usr)
        return web.Response(text=json.dumps({'status': 'success', 'message': 'User successfully created'}), status=200)
    except Exception as e:
        print(e)
        return web.Response(text=json.dumps({'status': 'Failure', 'message': str(e)}), status=500)


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', handler)
    # http: // localhost: 8080/
    app.router.add_post('/adduser', new_user)
    # http://localhost:8080/adduser?name=sudhanshu

    # Running The Server
    web.run_app(app, host='localhost')