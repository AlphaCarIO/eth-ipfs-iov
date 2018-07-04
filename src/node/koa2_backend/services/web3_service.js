import web3wrapper from '../utils/web3wrapper'

var BigNumber = require('bignumber.js')
BigNumber.config({ DECIMAL_PLACES: 18 })

export async function balanceOf(ctx) {
  let address = ctx.params.address
  await web3wrapper.then(result => {
    let balance = new BigNumber(result.tokenIns.balanceOf(address)).div(1e+18);
    ctx.response.body = { 
      'error_code': 0, 
      'error_msg': '', 
      data: { 
        'balance': balance, 
        'balance_fmt': balance.toFormat(18) 
      }
    }
  }).catch(function(err) {
    ctx.response.body = { 
      'error_code': -1, 
      'error_msg': err
    }
  });
}

export async function info(ctx) {
  await web3wrapper.then(result => {
    let symbol = result.tokenIns.symbol();
    let name = result.tokenIns.name();
    let decimals = result.tokenIns.decimals();
    let totalSupply = new BigNumber(result.tokenIns.totalSupply());
    let owner = result.tokenIns.owner();
    
    ctx.response.body = {
      'error_code': 0,
      'error_msg': '', 
      data: { 
        'symbol': symbol, 
        'name': name, 
        'decimals': decimals,
        'totalSupply': totalSupply,
        'owner': owner 
      }
    }
  }).catch(function(err) {
    ctx.response.body = { 
      'error_code': -1, 
      'error_msg': err 
    }
  });
}

