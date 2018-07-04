const router = require('koa-router')()

router.get('/', async (ctx, next) => {
  ctx.response.type = 'json';
  ctx.response.body = { 'name': 'AlphaCar BlockChain API', 'website': 'https://www.alphacar.io' };
})

//e.g. http://localhost:3000/token/balanceof/0xda83aee0f49802a331d455f503341a5fdcbde923
router.get('/greeting/:name', async (ctx, next) => {
  let name = ctx.params.name;
  ctx.response.body = "Hello, " + name + ". This is AlphaCar.IO.";
})

module.exports = router
