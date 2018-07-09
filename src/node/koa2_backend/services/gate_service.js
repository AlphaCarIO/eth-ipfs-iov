//import gate from '../utils/gate'
import gate_axios from '../utils/gate_axios'

export async function getPrice(ctx) {
  let param = ctx.params.ticker_pair

  await gate_axios.service.get(gate_axios.TICKER_URL + param)
    .then(function (response) {
      if (response.status == 200) {
        console.log('response.data:', response.data)
        console.log('last:', response.data.last)
        let price = parseFloat(response.data.last)
        let result = {
          'error_code': 0,
          'error_msg': '',
          data: {
            'price': price
          }
        }
        console.log('result:', result)
        ctx.response.body = result
      } else {
        ctx.response.body = {
          'error_code': -1,
          'error_msg': 'wrong status code',
        }
      }
    })
    .catch(function (error) {
      ctx.response.body = {
        'error_code': -1,
        'error_msg': error
      }
    });
}