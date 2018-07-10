const router = require('koa-router')()

import * as mongo_service from "../services/mongo_service"

router.get('/ubi_info/latest',async (ctx, next) => {
    ctx.response.type = 'json';
    await mongo_service.latestUBIInfo(ctx)
    await next()
})

router.get('/ubi_info/index/:ubi_code', async (ctx, next) => {
    ctx.response.type = 'json';
    await mongo_service.getUBIInfoByCode(ctx)
    await next()
})

router.get('/ubi_info/list', async (ctx, next) => {
    ctx.response.type = 'json';
    await mongo_service.getUBIInfoList(ctx)
    await next()
})

router.post('/ubi_info/tx_count_lst', async (ctx, next) => {
    ctx.response.type = 'json';
    await mongo_service.getTxCountList(ctx)
    await next()
})

module.exports = router
