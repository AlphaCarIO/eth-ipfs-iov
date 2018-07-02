import getWeb3 from '../libs/getWeb3'
var BigNumber = require('bignumber.js')
BigNumber.config({ DECIMAL_PLACES: 18 })

export async function balanceOf(address, ctx) {
  ctx.response.type = 'json';
  await getWeb3.then(result => {
    let balance = new BigNumber(result.tokenIns.balanceOf(address)).div(1e+18);
    ctx.response.body = { 'error_code': 0, 'error_msg': '', 
      data: { 'balance': balance, 'balance_fmt': balance.toFormat(18) }}
  }).catch(function(err) {
    ctx.response.body = { 'error_code': -1, 'error_msg': err }
  });
}
