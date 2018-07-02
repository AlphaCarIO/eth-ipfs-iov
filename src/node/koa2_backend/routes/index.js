const router = require('koa-router')()

import getWeb3 from '../libs/getWeb3'
import * as web3_service from "../services/web3_service"

router.get('/', async (ctx, next) => {
  ctx.response.type = 'json';
  ctx.response.body = { 'msg': 'demo MSG' };
})

//e.g. http://localhost:3000/token/balanceof/0xda83aee0f49802a331d455f503341a5fdcbde923
router.get('/token/balanceof/:address', async (ctx, next) => {
  await web3_service.balanceOf(ctx.params.address, ctx)
})

module.exports = router
