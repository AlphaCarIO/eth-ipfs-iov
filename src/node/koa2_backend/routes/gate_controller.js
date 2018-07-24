const router = require('koa-router')()

import * as gate_service from "../services/gate_service"

router.get('/api/gateio/ticker/:ticker_pair', async (ctx, next) => {
  ctx.response.type = 'json';
  await gate_service.getPrice(ctx)
})

module.exports = router
