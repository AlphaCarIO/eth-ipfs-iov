import axios from 'axios';
import * as config from "../config/config"

const service = axios.create(config.gate_query_conf)

service.interceptors.response.use(
    function(response) {
      return Promise.resolve(response)
    },
    function(error) {
      return Promise.reject(error)
    }
)

const TICKER_URL = '/api2/1/ticker/';

const USER_AGENT = '';

const HEADERS = {
    'User-Agent' : USER_AGENT,
    'Content-Type':'application/json',
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Authorization, Origin, X-Requested-With, Content-Type, Accept"
}

var gate_axios = {

    TICKER_URL: TICKER_URL,

    service: service,

};

export default gate_axios;
