const router = require('koa-router')()

import * as web3_service from "../services/web3_service"

router.get('/token/info', async (ctx, next) => {
  ctx.response.type = 'json';
  web3_service.info(ctx)
})

//e.g. http://localhost:3000/token/balance_of/0xda83aee0f49802a331d455f503341a5fdcbde923
router.get('/token/balance_of/:address', async (ctx, next) => {
  ctx.response.type = 'json';
  web3_service.balanceOf(ctx)
})

module.exports = router
