# importing stuff
from aiohttp import web
import aiohttp
from aiohttp.web import middleware
import json
import ccxt
from requests.api import request
import models
from models import Coin
from sqlalchemy.orm import Session
from db import session
from db import engine

# getting kucoin exchange
kucoin = ccxt.kucoin()
# aiohttp for server
routes = web.RouteTableDef()
# db creating
models.Base.metadata.create_all(bind=engine)


# http response codes
@middleware
async def middleware(request, handler):
    resp = await handler(request)
    resp.text = resp.text
    return resp


@routes.get('/price/{currency}')
async def price(request):
    try:
        coin = (request.match_info['currency']).upper()
        response = kucoin.fetch_ticker(f'{coin}/USDT')
        symbol = response['symbol']
        bid = response['bid']
        timestamp = response['timestamp']//1000
        response_obj = {
            'currency': symbol,
            'price': bid,
            'date': timestamp
        }
        coin_ = Coin()
        coin_.currency = symbol
        coin_.price = bid
        coin_.date = timestamp
        session.add(coin_)
        session.commit()
        session.close()
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception:
        raise aiohttp.web.HTTPBadRequest


@routes.get('/price/history/')
async def price_return(request):
    page = request.rel_url.query.get('page')
    coins_db = session.query(Coin).limit(10).offset((int(page)-1)*10)
    output = []
    for coin in coins_db:
        response_obj = {'id': coin.id,
                        'symbol': coin.currency,
                        'bid': coin.price,
                        'timestamp': coin.date
                        }
        output.append(response_obj)
    response = {'results': output}
    return web.Response(text=json.dumps(response), status=200)


@routes.delete('/price/history')
async def price_delete(request):
    await Coin.__table__.drop(engine)
    return web.Response(text='DELETE TABLE', status=200)


async def init():
    app = web.Application(middlewares=[middleware])
    app.router.add_routes(routes)
    return app


if __name__ == '__main__':
    web.run_app(init())
