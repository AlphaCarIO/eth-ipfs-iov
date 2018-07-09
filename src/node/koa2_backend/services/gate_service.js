//import gate from '../utils/gate'
import gate_axios from '../utils/gate_axios'

export async function getPrice(ctx) {
  let param = ctx.params.ticker_pair

  await gate_axios.service.get(gate_axios.TICKER_URL + param)
    .then(function (response) {
      if (response.status == 200) {
        let quoteVolume = parseFloat(response.data.quoteVolume)
        let baseVolume = parseFloat(response.data.baseVolume)
        let highestBid = parseFloat(response.data.highestBid)
        let high24hr = parseFloat(response.data.high24hr)
        let last = parseFloat(response.data.last)
        let lowestAsk = parseFloat(response.data.lowestAsk)
        let elapsed = response.data.elapsed
        let result = response.data.last == "true" ? true : false;
        let low24hr = parseFloat(response.data.low24hr)
        let percentChange = parseFloat(response.data.percentChange)
        let _result = {
          'error_code': 0,
          'error_msg': '',
          data: {
            'quoteVolume': quoteVolume,
            'baseVolume': baseVolume,
            'highestBid': highestBid,
            'high24hr': high24hr,
            'last': last,
            'lowestAsk': lowestAsk,
            'elapsed': elapsed,
            'result': result,
            'low24hr': low24hr,
            'percentChange': percentChange,
          }
        }
        console.log('result:', _result)
        ctx.response.body = _result
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